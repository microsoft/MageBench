from .planbase import Plan
import re, os, json, base64
from copy import deepcopy
from env.utils import resize_image


def get_range(string, tp):
    if string.startswith(f"```{tp}"):
        if "```" in string[len(f"```{tp}"):]:
            return string[len(f"```{tp}"):].find("```") + len(f"```{tp}")
        else:
            return len(string)
    return None

def get_range_auto(string):
    if "```" in string[len(f"```"):]:
        code_ed = string[len(f"```"):].find("```") + len(f"```")
        code = string[len(f"```"):code_ed]
    else:
        code_ed = len(string)
        code = string[len(f"```"):]
    
    if code.count("<") + code.count(">") > code.count("\n"):
        return "html", code_ed
    elif ";" in code or "function " in code or "document." in code or "const" in code:
        return "javascript", code_ed
    elif code.count("{") + code.count("}") > 1:
        return "css", code_ed
    
    return None, None

class OnlinePlan(Plan):

    def generate_with_continue(self, message, parse):
        out_text = self.generator(message, self.para, lambda x: x)
        new_out = ""
        if out_text.count("```") % 2 == 1:
            new_out = self.generator(message+[
                {
                    "role": "assistant",
                    "content": out_text
                },
                {
                    "role": "user",
                    "content": "continue the generate directly without any repetition."
                }
            ], self.para, lambda x: x)
        text = out_text + new_out
        return parse(text)
        
    def parse(self, ostring):
        args = []
        out = ostring
        ostring = ostring if "# Regenerate" not in ostring else ostring.split("# Regenerate")[1]
        # print("\n\n===out===\n\n", ostring)

        ostring = re.sub(r'\n+', '\n', ostring)
        ptr, ed = 0, len(ostring)

        while ptr < ed:
            if "```" not in ostring[ptr:]: 
                break
            ostr = ostring[ptr:]
            st = ostr.find("```")
            oidx = None
            TP = None
            for tp in ["html", "javascript", "css"]:
                oidx = get_range(ostr[st:], tp)
                if oidx is not None:
                    TP = tp
                    break

            if oidx is None:
                tp, oidx = get_range_auto(ostr[st:])
                if oidx is not None:
                    TP = tp

            if oidx is not None:
                code = ostr[st+len(f"```{TP}"): st+oidx]
                ptr += st + oidx + len("```")
                args.append({
                    "task_dir": self.env.sub_task_dir, 
                    "action": f"write_{TP}", 
                    "data": code
                })
            else:
                ptr += st + len("```")
        # print(args)

        return args, out
    
    def run(self, ActionCLS, debug=False, ):  # max_memory=20, max_loop=10, model_no_system=False, 

        task_prompt = self.env.task_prompt  # this code only run on GPT4O, Gemini and Claude
        
        message = [
            {
                "role": "system",
                "content": [{"type": "text", "text": self.env.system_prompt}]
            },
            {
                "role": "user",
                "content": task_prompt
            }
        ]

        # some model do not have system role
        if self.args.model_no_system:
            message = [{"role": "user", "content": [{"type": "text", "text": self.env.system_prompt}] + task_prompt}]
        
        parsing_err = 0

        for loop in range(1, self.args.max_loop+1):
            mem = []
            sts = self.env.trajectory.last_state
            cur_impl = ""
            if sts.cur_html != "":
                cur_impl += f"Current implementation: \n```html\n{sts.cur_html}\n```\n\n"
            if sts.cur_css is not None:
                cur_impl += f"```css\n{sts.cur_css}\n```\n\n"
            if sts.cur_js is not None:
                cur_impl += f"```javascript\n{sts.cur_js}\n```\n\n"
            
            if cur_impl != "":
                user_content = [
                                {
                                    "type": "text",
                                    "text": cur_impl
                                }
                            ]
                
                o = self.env.trajectory.last_observation
                for info in o.info:
                    if info["type"] == "image_url":
                        img = resize_image(info["image_url"], self.args.resolution)
                        img.save(self.env.tmp_dir + "/tmpp.png")
                        encoded_image = base64.b64encode(open(self.env.tmp_dir + "/tmpp.png", 'rb').read()).decode('ascii')
                        user_content.append({
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{encoded_image}"
                            }
                        })
                        break
                user_content.append({
                                    "type": "text",
                                    "text": """
Please adapt the code according to the current rendered screen shot of previous implementation, with this output format: 

# Analyze
Your Analyze
# Regenerate
re-generated code
If some of the files (e.g., javascript) do not need to be changed, just write '*javascript do not need to change*' and do not generate any javascript code, the same for html and css.
"""
                                })
                mem = {
                            "role": "user",
                            "content": user_content
                        }
            else:
                mem = {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": "There are no existing implementation, please implement all the code."
                                }
                            ]
                        }
            t_message = deepcopy(message) + [mem]
                
            # print("\n\n===message===\n\n", json.dumps([{ms["role"]: [(ct if isinstance(ct, str) or ct["type"]=="text" else "image") for ct in ms["content"]]} for ms in t_message], indent=4))
            acts, out = self.generate_with_continue(t_message, self.parse)
            # print(loop, [a["action"] for a in acts])
            # print(out)
            acts = [ActionCLS(**a) for a  in acts]
            
            
            imgs = 0
            d = False
            for idx, act in enumerate(acts):
                o, d = self.env.take_action(act)
                if d:
                    break
            if d:
                break
            if len(acts) == 0:
                parsing_err += 1
        
            r, d= self.env.Evaluator()
            open(os.path.join(self.env.tmp_dir, "output.txt"), "w").write(out)
            open(os.path.join(self.env.tmp_dir, "eval.json"), "w").write(json.dumps({
                "result": r,
                "details": d,
                "parsing_err": parsing_err
            }, indent=4))

            self.env.reset_tmp_dir(self.env.tmp_dir.replace(f"_loop{loop}", f"_loop{loop+1}"))
        return None, None








