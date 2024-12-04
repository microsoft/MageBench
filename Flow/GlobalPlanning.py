from .planbase import Plan
import re, os, json


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

class GlobalPlan(Plan):

    @property
    def special_prompt_for_task(self):
        if self.task == "WebUI":
            return [
                {
                    "type": "text",
                    "text": "Generate all necessary codes at a time. Your output should contain code blocks in markdown format, e.g., ```html\nxxxx```. generate javascript and css code if necessary. They will be writen to `index.html`, `script.js` and `style.css`."
                }
            ]
        elif self.task == "Sokoban":
            step_by_step = "Your output should follow this format: ### Analyze\nWrite a step by step planning to push all boxes to all targets.\n### Actions\na sequence of Left, Right, Up, Down, separate by ','"
            only_actions = "Generate all actions to fulfill the task at a time. Your output should follow this format: ### Analyze\n your analyze.\n### Actions\nA long sequence of Left, Right, Up, Down, separate by ','"
            return [
                {
                    "type": "text",
                    "text": f"Please analyze and directly output a list of actions to take. \n\n{only_actions}"
                }
            ]
        return 
    
    def parse(self, ostring):
        args = []
        out = ostring
        # print("\n\n===out===\n\n", ostring)

        if self.task == "WebUI":
            ostring = re.sub(r'\n+', '\n', ostring)
            ptr, ed = 0, len(ostring)

            fs = ostring.split("```")[1::2]
            for f in fs:
                fstrip = f.strip()
                tpidx = fstrip.find("\n")
                tp = fstrip[:tpidx]
                code = fstrip[tpidx+1:]
                args.append({
                        "task_dir": self.env.sub_task_dir, 
                        "action": f"write_{tp}", 
                        "data": code
                    })


            # while ptr < ed:
            #     if "```" not in ostring[ptr:]: 
            #         break
            #     ostr = ostring[ptr:]
            #     st = ostr.find("```")
            #     oidx = None
            #     TP = None
            #     for tp in ["html", "javascript", "css"]:
            #         oidx = get_range(ostr[st:], tp)
            #         if oidx is not None:
            #             TP = tp
            #             break

            #     if oidx is None:
            #         tp, oidx = get_range_auto(ostr[st:])
            #         if oidx is not None:
            #             TP = tp

            #     if oidx is not None:
            #         code = ostr[st+len(f"```{TP}"): st+oidx]
            #         ptr += st + oidx + len("```")
            #         args.append({
            #             "task_dir": self.env.sub_task_dir, 
            #             "action": f"write_{TP}", 
            #             "data": code
            #         })
            #     else:
            #         ptr += st + len("```")


        elif self.task == "Sokoban":
            if "### Actions" in ostring:
                ostring = ostring.split("### Actions")[1].strip()
            else:
                ostring = ostring.strip()
            als = [a.strip() for a in ostring.split(",")]
            for a in als:
                if a in ['Up', 'Down', 'Left', 'Right']:
                    args.append({
                        "name": a
                    })

        return args, out
    
    def run(self, ActionCLS, debug=False, **kwargs):

        task_prompt = []
        imgs = 0
        for ct in self.env.task_prompt:
            if ct["type"] == "text":
                task_prompt.append(ct)
            elif imgs < self.args.max_image:
                imgs += 1
                task_prompt.append(ct)
            else:
                task_prompt.append({
                    "type": "text",
                    "text": "image not available."
                })
        
        message = [
            {
                "role": "system",
                "content": self.env.system_prompt
            },
            {
                "role": "user",
                "content": task_prompt + self.special_prompt_for_task
            }
        ]
        if self.args.model_no_system:
            message = [{"role": "user", "content": [{"type": "text", "text": self.env.system_prompt}] + task_prompt + self.special_prompt_for_task}]
        # print("\n\n===message===\n\n", json.dumps([{ms["role"]: [(ct if isinstance(ct, str) or ct["type"]=="text" else "image") for ct in ms["content"]]} for ms in message], indent=4))
        
        acts, out = self.generator(message, self.para, self.parse)
        acts = [ActionCLS(**a) for a  in acts]
        for act in acts:
            o, d = self.env.take_action(act)
            if debug:
                pass
            if d:
                break
        r, d= self.env.Evaluator()
        open(os.path.join(self.env.tmp_dir, "output.txt"), "w").write(out)
        open(os.path.join(self.env.tmp_dir, "eval.json"), "w").write(json.dumps({
            "result": r,
            "details": d,
            "parsing_err": len(acts) == 0
        }, indent=4))
        return r, d








