from .planbase import Plan
import re, os, json, base64
from copy import deepcopy
from env.utils import resize_image

class OnlinePlan(Plan):

    @property
    def special_prompt_for_task(self):
        if self.task == "Football":
            return [
                {
                    "type": "text",
                    "text": f"You should perform 1 action for each generation, with this format: \n# analyze\nsome analyze\n# action\naction ID\n\nFor example: \n# analyze\n...\n# action\naction_left"
                }
            ]
        elif self.task == "Sokoban":
            return [
                {
                    "type": "text",
                    "text": f"You should perform 1 action for each generation, with this format: \n# analyze\nsome analyze\n# action\naction ID\n\nFor example: \n# analyze\n...\n# action\nUp"
                }
            ]
    def parse(self, ostring):
        args = []
        out = ostring
        # print("\n\n===out===\n\n", ostring)

        if "# action" in ostring:
            ostring = ostring.split("# action")[1].strip()
        ac = ostring.strip()
        if self.task == "Sokoban" and ac in ['Up', 'Down', 'Left', 'Right']:
            args.append({
                    "name": ac
                })
        elif self.task == "Football" and ac in ['action_left', 'action_top_left', 'action_top', 'action_top_right', 'action_right', 'action_bottom_right', 'action_bottom', 'action_bottom_left', 'action_long_pass', 'action_high_pass', 'action_short_pass', 'action_shot', 'action_sprint', 'action_release_sprint', 'action_dribble', 'action_release_dribble']:
            args.append({
                    "name": ac
                })

        return args, out
    
    def run(self, ActionCLS, debug=False, ):  # max_memory=20, max_loop=10, model_no_system=False, 

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

        memory = [{
                "role": "user",
                "content": task_prompt + [{
                            "type": "text",
                            "text": "Please act according to the init game scene."
                        }]  # init task prompt
            }]
        
        message = [
            {
                "role": "system",
                "content": [{"type": "text", "text": self.env.system_prompt}]
            },
            {
                "role": "user",
                "content": self.special_prompt_for_task
            }
        ]

        # some model do not have system role
        if self.args.model_no_system:
            message = [{"role": "user", "content": [{"type": "text", "text": self.env.system_prompt}] + self.special_prompt_for_task}]
        
        max_images_for_memory = self.args.max_image
        assert max_images_for_memory > 0, "model max images is not enough for this task."

        parsing_err = 0

        for loop in range(self.args.max_loop):
            
            used_memory = min(len(memory), self.args.max_memory*2)
            memory = memory[-used_memory:]
            max_image_memory_index = 0
            memory_images = 0
            for i in range(-1, -used_memory-1, -1):
                memory_images += len(list(filter(lambda x: x["type"]=="image_url", memory[i]["content"])))
                if memory_images > max_images_for_memory:
                    break
                else:
                    max_image_memory_index = i
            
            assert max_image_memory_index < 0  # because i<0  !!!!!!
            max_image_memory_index = max_image_memory_index + len(memory)

            for id in range(len(memory)):
                if id < max_image_memory_index:  # clear images
                    cts = memory[id]["content"]
                    ncts = []
                    for ict in range(len(cts)):
                        if not cts[ict]["type"] == "image_url":
                            ncts.append(cts[ict])
                    memory[id]["content"] = ncts

            t_message = deepcopy(message) + memory
            # print("\n\n===message===\n\n", json.dumps([{ms["role"]: [(ct if isinstance(ct, str) or ct["type"]=="text" else "image") for ct in ms["content"]]} for ms in t_message], indent=4))
            acts, out = self.generator(t_message, self.para, self.parse) 
            open(os.path.join(self.env.tmp_dir, f"output_{loop}.txt"), "w").write(out)
            # print(out, [a["name"] for a in acts])
            acts = [ActionCLS(**a) for a  in acts]
            
            
            memory.append({
                        "role": "assistant",
                        "content": [{
                        "type": "text",
                        "text": out
                    }]})
            user_content = []
            d = False
            for idx, act in enumerate(acts):
                o, d = self.env.take_action(act)
                if o is None:
                    pass
                else:
                    for info in o.info:
                        if info["type"] == "text":
                            user_content.append(info)
                        else:
                            assert "image_url" in info, info
                            img = resize_image(info["image_url"], self.args.resolution)
                            img.save(self.env.tmp_dir + "/tmpp.png")
                            encoded_image = base64.b64encode(open(self.env.tmp_dir + "/tmpp.png", 'rb').read()).decode('ascii')
                            user_content.append({
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{encoded_image}"
                                }
                            })
                    
                if debug:
                    pass
                if d:
                    break
            if d:
                break
            if len(acts) == 0:
                parsing_err += 1
                user_content.append({
                            "type": "text",
                            "text": "Please regenerate the response that satisfy the format requirements strictly."
                        })
            else:
                user_content.append({
                            "type": "text",
                            "text": "Please continue to act according to the current game scene."
                        })
            if len(user_content)>0:
                memory.append({
                            "role": "user",
                            "content": user_content,
                })
                
        
        r, d= self.env.Evaluator()
        
        open(os.path.join(self.env.tmp_dir, "eval.json"), "w").write(json.dumps({
            "result": r,
            "details": d,
            "parsing_err": parsing_err
        }, indent=4))
        return r, d








