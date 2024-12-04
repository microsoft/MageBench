
import pickle as pk
from typing import List
from .base import Action, Observation, State, EnvTraj, AgentEnvironment
from copy import deepcopy
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os, base64, json
from .utils import resize_image

class SokobanState(State):
    def __init__(self):
        self.reward = []
        self.cur_best_reward = 0.0
        self.accumulate_reward = 0.0
        self.task_done = False

    @property
    def info(self, ):
        return [{
            "type": "text", 
            "text": f"accumulated reward: {self.accumulate_reward}\nBest reward: {self.cur_best_reward}"
        }]


class SokobanAction(Action):
    def __init__(self, name):

        self.tocode = {
            "Left": 3,
            "Right": 4,
            "Up": 1,
            "Down": 2,
            "Restart": -1,
        }
        assert name in self.tocode.keys()
        self.name = name
    def to_code(self):
        return self.tocode[self.name]


class SokobanEnv(AgentEnvironment):
    def __init__(self, sub_task_path, tmp_dir = "./tmp/Sokoban", img_size = 256):
        self.task = "Sokoban"
        self.sub_task_path = sub_task_path
        traj = EnvTraj()
        self.env = pk.load(open(self.sub_task_path, "rb"))
        init_state = SokobanState()
        traj.update("state", init_state)
        init_observation = self.env.render("rgb_array")
        init_ob = Observation()
        init_ob.add_image(Image.fromarray(init_observation))
        traj.update("observation", init_ob)
        super().__init__(traj)
        os.makedirs(tmp_dir, exist_ok=True)
        self.tmp_dir = tmp_dir
        self.img_max_size = img_size
        id = sub_task_path.rfind("/")
        self.done = False
        self.upper_reward = json.load(open(sub_task_path[:id+1] + "upper_bound.json"))[sub_task_path[id+1:].replace(".pkl", "")]["reward"]
    
    def take_action(self, act: Action):
        assert not self.done, "task is already done!!!"
        """take a action"""
        if act.name == "Restart":
            return self.restart()
        self.trajectory.update("action", act)
        _, reward, done, info = self.env.step(act.to_code())
        obser = self.env.render("rgb_array")
        # obser_state = self.env.render("tiny_rgb_array")
        img = Image.fromarray(obser)
        # if self.action_id<10:
        #     img.save(os.path.join(self.tmp_dir, f"action_{self.action_id}.png"))
        ob = None
        state = SokobanState()
        state.reward = deepcopy(self.trajectory.last_state.reward) + [reward]
        state.accumulate_reward = sum(state.reward)
        state.cur_best_reward = max(self.trajectory.last_state.cur_best_reward, state.accumulate_reward)
        state.task_done = done
        self.done = done
        self.trajectory.update("state", state)
        ob = Observation()
        ob.add_image(img)
        self.trajectory.update("observation", ob)
        return ob, done

 
    def Evaluator(self, ):
        """Evaluate the cur traj"""
        return (self.trajectory.last_state.cur_best_reward - self.upper_reward)*5 + 100, \
                self.trajectory.last_state.info
    
    def restart(self):
        traj = EnvTraj()
        self.env = pk.load(open(self.sub_task_path, "rb"))
        init_state = SokobanState()
        traj.update("state", init_state)
        init_observation = self.env.render("rgb_array")
        init_ob = Observation()
        init_ob.add_image(Image.fromarray(init_observation))
        traj.update("observation", init_ob)
        
        self.history_trojectory.append(deepcopy(self.trajectory))
        self.trajectory = traj

        return init_state, init_ob


    @property
    def system_prompt(self, ) -> str:
        '''system rule for this environment, including how to act and observation statements'''
        # - 'Get_Scene': Get the currently rendered game scene, remember to call this after few actions. 
        # - 'Restart': Restart the game, which will return to the initial state of the game.
        return """You're going to play a game of Sokoban, where the goal is to manipulate the green character to push the yellow box into the target area (an area with a red dot in the center). 
You'll use text commands to manipulate your character, and here are the action ID and explaination:
- 'Left': The action character moves to the left, and if there is a box on the left, pushes the box to the left.
- 'Right': The action character moves to the right, and if there is a box on the right, pushes the box to the right.
- 'Up': Character moves up, and if there is a box above, pushes the box up.
- 'Down': The action character moves down, and if there is a box underneath, pushes the box down.

Note: 
1. It is not possible to push two boxes side by side at the same time from the side-by-side direction.
2. The red brick pattern is the wall. The game can go into a lose-lose state, for example if you push the box into a corner where the corner is not the target area. In this case, you should restart the game.
"""

    @property
    def task_prompt(self, ) -> str:
        '''task description for this environment, for tasks that contain special requirements'''
        o = self.get_init_observation()
        init_ct = deepcopy(o.info)
        for t in init_ct:
            if t["type"] == "image_url":
                img = resize_image(t["image_url"], self.img_max_size)
                img.save(os.path.join(self.tmp_dir, "tmp.png"))
                encoded_image = base64.b64encode(open(os.path.join(self.tmp_dir, "tmp.png"), 'rb').read()).decode('ascii')
                t["image_url"] = {
                    "url": f"data:image/jpeg;base64,{encoded_image}"
                }

        return init_ct

    def Ending(self, ):
        imgs = []
        rws = []
        acs = []
        for tp, obj in  self.trajectory.traj:
            if tp == "observation":
                for ct in obj.info:
                    if ct["type"] == "image_url":
                        imgs.append(ct["image_url"])
            if tp == "state":
                rws.append(obj.accumulate_reward)
            if tp == "action":
                acs.append(obj.name)

        
        assert len(imgs) == len(rws), (len(imgs), len(rws))

        for i, img in enumerate(imgs):
            I1 = ImageDraw.Draw(img)
            try:
                I1.text((0, 0), "actions: "+ acs[i], fill=(255, 255, 255))
            except:
                pass
            I1.text((0, 20), "frame: "+ str(i), fill=(255, 255, 255))
            I1.text((0, 40), "reward: "+ str((rws[i] - self.upper_reward)*5 + 100) , fill=(255, 255, 255))

        image_arrays = [np.array(img) for img in imgs]  
    
        # Set the duration for each image (seconds per image)  
        fps = 2 # frames per second  
        
        # Create the video clip  
        from moviepy.editor import ImageSequenceClip 
        clip = ImageSequenceClip(image_arrays, fps=fps)  
        
        # Output file path  
        output_video_path = f"{self.tmp_dir}/output_video.mp4"
        
        # Write the video file  
        clip.write_videofile(output_video_path, codec='libx264')
if __name__ == "__main__":
    env = SokobanEnv("/data/home/t2vg-a100-G4-35/zms/LMMAgentBench/resources/Sokoban/185-Sokoban-large-v1.pkl")
    o = env.get_init_observation()
    o.info[0]["image_url"].save("test.png")
    acs = []

    while True:
        acts = input()
        acs.append(acts)
        act = SokobanAction(acts)
        o = env.take_action(act)
        print(s.info)
        o.info[0]["image_url"].save("test.png")
    print(acs)
