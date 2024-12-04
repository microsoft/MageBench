


import pickle as pk
from typing import List
from .base import Action, Observation, State, EnvTraj, AgentEnvironment
from copy import deepcopy
from PIL import Image
import os
from .utils import get_driver, evaluate_different_interaction
import platform
import re, base64
from .utils import resize_image


def split_string(input_string):
    pattern = r'(?:!\[.*\]\((.*?)\))'
    parts = re.split(pattern, input_string)
    return [part for part in parts if part]


def md_to_json(md, dir, tmp_dir, max_size):
    splited_md = split_string(md)
    content = []
    for t in splited_md:
        if not t.endswith(".png"):
            content.append({
                "type": "text",
                "text": t
            })
        else:
            if t.startswith("./"):
                t = t.strip("./")
            img_dir = dir + "/" + t
            img = Image.open(img_dir).convert("RGB")
            img = resize_image(img, max_size)
            img.save(tmp_dir + "/tmpp.png")
            encoded_image = base64.b64encode(open(tmp_dir + "/tmpp.png", 'rb').read()).decode('ascii')
            os.remove(tmp_dir + "/tmpp.png")
            content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{encoded_image}"
                }
            })
    return content

class WebUIState(State):
    def __init__(self):
        self.cur_html = ""
        self.cur_js = None
        self.cur_css = None

    @property
    def info(self, ):
        files_text = f"Current implementation:\n```html\n{self.cur_html}\n```\n\n"
        if self.cur_js is not None:
            files_text += f"```javascript\n{self.cur_js}\n```\n\n"
        if self.cur_css is not None:
            files_text += f"```css\n{self.cur_css}\n```\n\n"
        # TODO: available actions ?
        return [{
            "type": "text", 
            "text": files_text
        }]


class WebUIAction(Action):
    def __init__(self, task_dir, action, data):
        self.action = action
        self.inputs = data
        gbs = {}
        exec(open(os.path.join(task_dir, "actions.py"), encoding='utf-8').read(), gbs, gbs)
        self.available_actions = {f.__name__: f for f in gbs["actions"]}
        assert action in list(self.available_actions.keys())+["refresh", "write_html", "write_javascript", "write_css"], action

    
    def act(self, driver, tmp_dir, last_state):
        state = deepcopy(last_state)
        observation = None
        if self.action in self.available_actions:
            try:
                self.available_actions[self.action](driver)
                driver.save_screenshot(os.path.join(tmp_dir, "last_ob.png"))
                observation = Image.open(os.path.join(tmp_dir, "last_ob.png")).convert("RGB")
            except:
                observation = None
        elif self.action == "refresh":
            driver = get_driver(os.path.join(tmp_dir, "index.html"))
            driver.save_screenshot(os.path.join(tmp_dir, "last_ob.png"))
            observation = Image.open(os.path.join(tmp_dir, "last_ob.png")).convert("RGB")
        elif self.action == "write_html":
            state.cur_html = self.inputs
            
        elif self.action == "write_javascript":
            state.cur_js = self.inputs
            
        elif self.action == "write_css":
            state.cur_css = self.inputs
            
        
        if state.cur_html != "":
            open(os.path.join(tmp_dir, "index.html"), "w", encoding="utf-8").write(state.cur_html)
        if state.cur_js is not None:
            open(os.path.join(tmp_dir, "script.js"), "w", encoding="utf-8").write(state.cur_js)
        if state.cur_css is not None:
            open(os.path.join(tmp_dir, "style.css"), "w", encoding="utf-8").write(state.cur_css)
        return driver, state, observation
        

class WebUIEnv(AgentEnvironment):
    def __init__(self, sub_task_dir, tmp_dir="./tmp/WebUI", img_size = 256):
        self.task = "WebUI"
        self.sub_task_dir = sub_task_dir
        gbs = {}
        exec(open(os.path.join(sub_task_dir, "actions.py"), encoding="utf-8").read(), gbs, gbs)
        self.all_actions =  ["refresh"]+[f.__name__ for f in gbs["actions"]]
        
        traj = EnvTraj()
        init_state = WebUIState()
        traj.update("state", init_state)
        init_ob = Observation()
        traj.update("observation", init_ob)  # empty observation
        super().__init__(traj)
        self.img_max_size = img_size

        self.driver = None
        # tmp_dir = tmp_dir.replace(sub_name, "")
        os.makedirs(tmp_dir, exist_ok=True)
        sys = platform.system()
        if sys == "Windows":
            os.system(f"xcopy /E /I \"{sub_task_dir}\"/* \"{tmp_dir}\"") 
        elif sys == "Linux":
            os.system(f"cp -r '{sub_task_dir}'/* '{tmp_dir}'/")
        for f in ["index.html", "style.css", "script.js"]:
            if os.path.exists(os.path.join(tmp_dir, f)):
                os.remove(os.path.join(tmp_dir, f))
        self.tmp_dir = tmp_dir
        self.task_content = md_to_json(open(os.path.join(sub_task_dir, "tasks.md"), encoding="utf-8").read(), sub_task_dir, tmp_dir, img_size)
    

    # this is for online setting
    def reset_tmp_dir(self, new_tmp):
        os.makedirs(new_tmp, exist_ok=True)
        sys = platform.system()
        if sys == "Windows":
            os.system(f"xcopy /E /I \"{self.sub_task_dir}\"/* \"{new_tmp}\"") 
        elif sys == "Linux":
            os.system(f"cp -r '{self.sub_task_dir}'/* '{new_tmp}'/")
        for f in ["index.html", "style.css", "script.js"]:
            if os.path.exists(os.path.join(new_tmp, f)):
                os.remove(os.path.join(new_tmp, f))
        self.tmp_dir = new_tmp

    def start_from_exists(self, exists_dir):
        '''
        starting from a exist code, this is for online debuging experiment in the paper
        pretend we have done an action once
        '''
        act = WebUIAction(task_dir=self.sub_task_dir, action="refresh", data = None)
        self.trajectory.update("action", act)

        self.driver = get_driver(os.path.join(exists_dir, "index.html"))
        self.driver.save_screenshot(os.path.join(self.tmp_dir, "last_ob.png"))

        state = deepcopy(self.trajectory.last_state)
        if os.path.exists(os.path.join(exists_dir, "index.html")):
            state.cur_html = open(os.path.join(exists_dir, "index.html"), encoding='utf-8').read()
        if os.path.exists(os.path.join(exists_dir, "style.css")):
            state.cur_css = open(os.path.join(exists_dir, "style.css"), encoding='utf-8').read()
        if os.path.exists(os.path.join(exists_dir, "script.js")):
            state.cur_js = open(os.path.join(exists_dir, "script.js"), encoding='utf-8').read()
        self.trajectory.update("state", state)

        ob = Observation()
        ob_img = Image.open(os.path.join(self.tmp_dir, "last_ob.png")).convert("RGB")
        if ob_img is not None:
            ob.add_image(ob_img)
        else:
            ob.add_text("No rendering image got, please ensure the code is correct and the corresponding tag's name/class/id is as description required.\n")
        self.trajectory.update("observation", ob)


    def take_action(self, act: Action):
        """take a action"""
        self.trajectory.update("action", act)
        self.driver, state, ob_img = act.act(self.driver, self.tmp_dir, self.trajectory.last_state)
        
        if state is not None:
            self.trajectory.update("state", state)
        
        # print("@@@@@@@@1111", self.all_actions)
        ob = Observation()
        for ac in self.all_actions:
            obac = WebUIAction(task_dir=self.sub_task_dir, action=ac, data = None)
            self.driver, state, ob_img = obac.act(self.driver, self.tmp_dir, self.trajectory.last_state)
            ob.add_text("Rendered image after action: "+ ac+"\n")
            if ob_img is not None:
                ob.add_image(ob_img)
            else:
                ob.add_text("Action failed and no rendering image got, please ensure the interation is implemented, and corresponding tag's name/class/id is as description required.\n")
            
        self.trajectory.update("observation", ob)
        # print("@@@@@@@@2222", [info["type"] for info in ob.info])
        return ob, False

    
    def Evaluator(self, ):
        """Evaluate the cur traj"""
        taget_html = os.path.join(self.sub_task_dir, "index.html")
        generated_html = os.path.join(self.tmp_dir, "index.html")
        acs = os.path.join(self.sub_task_dir, "actions.py")
        res, details = evaluate_different_interaction(taget_html, generated_html, acs)
        return res, details



    @property
    def system_prompt(self, ) -> str:
        '''system rule for this environment, including how to act and observation statements'''
        # 'refresh' - Input: None, open and refresh the webpage to its initial state and return the screen shot, please do this as next action after you edict the code. 
        # {acts}
        # acts = ""
        # for a in self.all_actions:
        #     acts += f"'{a}' - Input: None, present the action named: {a} to current webpage, and return the screen shot. The settings of the action are the same as in the description.\n"
        return f"""Your job is to re-implement a Web page UI given target description and screen shot, by coding with `index.html`, and probably `style.css` and `script.js` if needed.
You will be provided a task description and available actions. Actions including writing to files and interact with your generated webpage.
Here are the action ID and explaination:

'write_html' - Input: str, Write the input str into 'index.html', if called second times, it will override the file.
'write_javascript' - Input: str, Write the input str into 'script.js', if called second times, it will override the file.
'write_css' - Input: str, Write the input str into 'style.css', if called second times, it will override the file.
"""

    @property
    def task_prompt(self, ) -> str:
        '''task description for this environment, for tasks that contain special requirements'''
        return self.task_content

    
    def Ending(self, ):
        md_file = ""
        os.makedirs(os.path.join(self.tmp_dir, "out_images"), exist_ok=True)
        for idx, (tp, obj) in enumerate(self.trajectory.traj):
            if tp == "observation":
                md_file += f"\n# observation-{idx}\n"
                for ifo, ct in enumerate(obj.info):
                    if ct["type"] == "image_url" and ct["image_url"] is not None:
                        imgp = os.path.join(self.tmp_dir, "out_images", f"o-{idx}-d-{ifo}.jpg")
                        ct["image_url"].save(imgp)
                        md_file += f"\n![o-{idx}-d-{ifo}](out_images/o-{idx}-d-{ifo}.jpg)\n"
                    elif ct["type"] == "text":
                        md_file += ct["text"]
            if tp == "state":
                md_file += f"\n# state-{idx}\n"
                md_file += obj.info[0]["text"]
            if tp == "action":
                md_file += f"\n# action-{idx}\n"
                md_file += "\n" + obj.action + "\n"
        open(os.path.join(self.tmp_dir, "output_progress.md"), "w", encoding="utf-8").write(md_file)
        if self.driver is not None:
            self.driver.quit()


if __name__ == "__main__":
    td = "/data/home/t2vg-a100-G4-35/zms/LMMAgentBench/resources/WebUI/Card1"
    env = WebUIEnv(td)
    print(env.system_prompt)
    print(env.task_prompt)
    d = """
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Creative Card 1</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <section class="card-container">
      <article class="content">
        <h2 data-filter-by="text" data-evalby="font-size">Title</h2>
        <p data-filter-by="text" data-evalby="line-height|padding|margin">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde adipisci
          placeat enim omnis rem vero hic, saepe quis fugiat? Molestiae
          consectetur, esse quidem at magni explicabo ab est suscipit odit?
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dicta
          laborum dolorum eos libero enim illum rem, aliquid voluptatibus
          obcaecati tenetur consequuntur nihil aut a officia culpa molestias?
          Nostrum, temporibus ea!
        </p>
        <a href="" data-filter-by="text" data-evalby="font-size|color|background|padding">Read More</a>
      </article>
    </section>
  </body>
</html>
"""
    act = WebUIAction(td, "write_html", d)
    o = env.take_action(act)
    d = """
body {
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: sans-serif;
  background: rgb(10, 10, 10);
  height: 100vh;
}

.card-container {
  position: relative;
  width: 320px;
  padding: 40px;
  background: white;
  overflow: hidden;
}

.card-container:before {
  content: "";
  position: absolute;
  left: 0;
  bottom: calc(-100% + 5px);
  width: 100%;
  height: 100%;
  background: blueviolet;
  z-index: 1;
  transition: 1s;
}

.card-container:hover:before {
  bottom: 0;
}

.content {
  position: relative;
  color: #000;
  z-index: 2;
  transition: 1s;
}

h2 {
  font-size: 30px;
}

p {
  line-height: 25px;
  padding: 20px 0;
  margin: 20px 0;
}

a {
  font-size: 12px;
  color: #fff;
  text-decoration: none;
  background: rgb(22, 7, 35);
  padding: 0.6rem 1rem;
}

.card-container:hover .content {
  color: #fff;
}

"""
    act = WebUIAction(td, "write_css", d)
    o = env.take_action(act)
    print(o)
    act = WebUIAction(td, "refresh", None)
    o = env.take_action(act)
    r, d= env.Evaluator()
    print(r)

