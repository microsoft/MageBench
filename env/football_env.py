from typing import List
from .base import Action, Observation, State, EnvTraj, AgentEnvironment
from copy import deepcopy
from PIL import Image, ImageEnhance
import os, base64, json
from .utils import resize_image, football_config
import numpy as np
from PIL import ImageDraw, ImageFont

from gfootball.env import football_env



class FootballState(State):
    def __init__(self):
        self.reward = []
        self.accumulate_reward = 0.0
        self.task_done = False
        self.detailed_reward = []

    @property
    def info(self, ):
        return [{
            "type": "text", 
            "text": f"accumulated reward: {self.accumulate_reward}"
        }]


class FootballAction(Action):
    def __init__(self, name):

        self.tocode = {
            'action_idle': 0,
            'action_left': 1,
            'action_top_left': 2,
            'action_top': 3,
            'action_top_right': 4, 
            'action_right': 5, 
            'action_bottom_right': 6, 
            'action_bottom': 7, 
            'action_bottom_left': 8,
            'action_long_pass': 9,
            'action_high_pass': 10,
            'action_short_pass': 11,
            'action_shot': 12,
            'action_sprint': 13,
            'action_release_direction': 14,
            'action_release_sprint': 15,
            'action_sliding': 16,
            'action_dribble': 17,
            'action_release_dribble': 18,
            'action_builtin_ai': 19 
        }
        self.toname = {v:k for k, v in self.tocode.items()}
        if name not in self.tocode.keys():
            self.name = "action_idle"
        else:
            self.name = name
    def to_code(self, oname=None):
        if oname is None:
            return self.tocode[self.name]
        else:
            return self.tocode[oname]
    def to_name(self, code=None):
        if code is None:
            return self.name
        else:
            return self.toname[code]

  
def HARDCODE_IMAGE_AUGMENTATION(image):
    """
    If your system opengl library, linux version, GPU type do not match perfectly(expecially on A100), the rendered image may have some color issues.
    One ugly but fast solution is to directly adjust the rendered images.

    If your environ do not have such issues, clear those code and just return the image.
    """
    bright_enhancer = ImageEnhance.Brightness(image)
    image = bright_enhancer.enhance(1.5)
    contrast_enhancer = ImageEnhance.Contrast(image)
    image = contrast_enhancer.enhance(0.6)
    bright_enhancer = ImageEnhance.Brightness(image)
    image = bright_enhancer.enhance(1.2)
    return image



class FootballEnv(AgentEnvironment):
    def __init__(self, sub_task_path, tmp_dir = "./tmp/Football", img_size = 1280, 
                 use_bot = False, use_adapting_render=True):
        # hyper para
        self.task = "Football"
        self.NSTEPS = 400 # task description
        self.MAX_AUTO_STEPS = 10
        self.MOVE_MIN_DISTANCE = 0.01
        
        
        self.sub_task_path = sub_task_path
        self.use_bot = use_bot
        traj = EnvTraj()


        # env
        agent = 'bot' if self.use_bot else 'agent'
        cfg_values = {
            'action_set': 'full',
            'dump_full_episodes': True,
            'players': [f'{agent}:left_players=1'], 
            'real_time': False,
            'level': self.sub_task_path
        }
        cfg = football_config(cfg_values, self.sub_task_path)
        self.env = football_env.FootballEnv(cfg)

        init_state = FootballState()
        traj.update("state", init_state)
        init_observation = self.env.render("rgb_array")
        init_ob = Observation()
        img = Image.fromarray(init_observation)
        img = HARDCODE_IMAGE_AUGMENTATION(img)
        init_ob.add_text("Current game scene:")
        init_ob.add_image(img)
        traj.update("observation", init_ob)
        super().__init__(traj)
        os.makedirs(tmp_dir, exist_ok=True)
        self.tmp_dir = tmp_dir
        self.img_max_size = img_size
        self.done = False
        self.history_env_states = []
        self.reward_utils = None
        self.auto_acting_utils = None
        self.use_adapting_render = use_adapting_render
        self.auto_acting = False
        
    def take_action(self, act: Action):

        if not self.use_adapting_render or len(self.history_env_states)==0:  # first step
            return self._take_action(act)
        
        assert not self.use_bot, "auto rendering is not compatable with bot, use action built-in ai instead"
        
        if self.auto_acting_utils is None:
            self.auto_acting_utils = {
                "prev_act": -1,  # for shoting, passing, moving
                "prev_direction": 5,  # for passing, shoting
                "auto_mode": None,
                "auto_steps": 0,   # only work for moving
                "perform_pass_player": -1
            }
        assert not self.auto_acting, "remember to return the auto_acting flag after auto acting"
        assert self.auto_acting_utils["auto_steps"] == 0 and self.auto_acting_utils["auto_mode"] is None and self.auto_acting_utils["perform_pass_player"] == -1, "remember to reset auto utils"

        state = self.history_env_states[-1]

        if act.to_code() in [1,2,3,4,5,6,7,8]: #moving
            self.auto_acting_utils["prev_direction"] = act.to_code()
            if self.auto_acting_utils["prev_act"] == -1:  # very begin
                self.auto_acting_utils["prev_act"] = act.to_code()
                return self._take_action(act)
            elif self.auto_acting_utils["prev_act"] == act.to_code():  # moving in a same direction, start auto-acting
                self.auto_acting = True  # go to auto acting, acting by moving
                self.auto_acting_utils["auto_mode"] = "move"
            else:
                # other action (direction) -> move action
                self.auto_acting_utils["prev_act"] = act.to_code()
                return self._take_action(act)
        elif act.to_code() in [9, 10, 11, 12] and state["ball_owned_player"] != -1:
            self.auto_acting = True  # go to auto acting, acting by pass
            self.auto_acting_utils["auto_mode"] = "pass"
            self.auto_acting_utils["perform_pass_player"] = state["ball_owned_player"]
            self.auto_acting_utils["prev_act"] = act.to_code()
        else:
            # other actions that do not support auto-acting
            self.auto_acting_utils["prev_act"] = act.to_code()
            return self._take_action(act)

                
        # auto_acting

        o, d = None, None
        while self.auto_acting:
            if self.auto_acting_utils["auto_mode"] == "move":
                # take action!
                o, d = self._take_action(act)
                state = self.history_env_states[-1]
                if not self.check_move_or_not(state) or d or self.auto_acting_utils["auto_steps"] >= self.MAX_AUTO_STEPS-1:
                    self.auto_acting = False
                else:
                    # continue to move on same direction, but with max auto time
                    self.auto_acting_utils["auto_steps"] += 1
            elif self.auto_acting_utils["auto_mode"] == "pass":
                '''
                In this case, we will do: (direction, pass, direction, pass ... ) untill the ball left the control of perform_pass_player
                After the ball_owned_player=-1 (ball passed in air), we will do built-in-ai action untill one of teamate receive the ball.
                '''
                if state["ball_owned_player"] == self.auto_acting_utils["perform_pass_player"]:
                    # take action!
                    o, d = self._take_action(act)   # pass/shot action
                    if d: break
                    direction = FootballAction(act.to_name(self.auto_acting_utils["prev_direction"]))
                    o, d = self._take_action(direction)   # direction action
                    if d: break
                    state = self.history_env_states[-1]
                    continue
                elif state["ball_owned_player"] == -1:
                    # the ball is in air !!!
                    auto = FootballAction('action_builtin_ai')
                    o, d = self._take_action(auto)   # auto untill receive the ball
                    if d: break
                    state = self.history_env_states[-1]
                else:
                    # the ball passed finished! we leave here for model to do other action
                    self.auto_acting = False
                    self.auto_acting_utils["prev_act"] = act.to_code()
            else:
                assert False, "auto mode not found!!!! must be pass or move"


                
        self.auto_acting_utils["auto_steps"] = 0
        self.auto_acting_utils["auto_mode"] = None
        self.auto_acting_utils["perform_pass_player"] = -1

        return o, d


    def check_move_or_not(self, state, ) -> bool:
        '''
        if continue to move (no opponents arround), return True else False
        '''
        pos_now = np.array(state["ball"][:2])
        direction_now = np.array(state["ball_direction"][:2])
        if state["ball_owned_player"] != -1:
            pos_now = np.array(state["left_team"][state["ball_owned_player"]])
            direction_now = np.array(state["left_team_direction"][state["ball_owned_player"]])
        
        pos_3 = pos_now + direction_now * 3

        # out of field
        if pos_3[0] >= 1.0 or pos_3[0] <= -1.0 or pos_3[1] >= 0.42 or pos_3[1] <= -0.42:
            return False
        
        apponents_now = np.array(state["right_team"])
        apponents_direction = np.array(state["right_team_direction"])
        
        for i in range(0, 6):
            my_pos = pos_now + i * direction_now
            apponents_pos = apponents_now + i * apponents_direction
            for appo in apponents_pos:
                if np.linalg.norm(my_pos - appo) < self.MOVE_MIN_DISTANCE:
                    return False
        
        return True




        

    def _take_action(self, act: Action):
        assert not self.done, "task is already done!!!"
        """take a action"""
        self.trajectory.update("action", act)

        if self.use_bot:
            env_state, _, done, info = self.env.step([])
        else:
            env_state, _, done, info = self.env.step(act.to_code())

        if not isinstance(env_state, dict):
            env_state = env_state[0]
        
        img = Image.fromarray(env_state["frame"])
        img = HARDCODE_IMAGE_AUGMENTATION(img)


        # if self.action_id<10:
        #     img.save(os.path.join(self.tmp_dir, f"action_{self.action_id}.png"))
        ob = None
        state = FootballState()
        try:
            to_act = act.tocode["action_"+str(self.env._env._trace[-1]['debug']['action'][0])]
        except:
            to_act = act.to_code()
        rw, detail = self.get_reward(env_state, to_act, done)
        done = self.reward_utils["task_done"] or done
        state.reward = deepcopy(self.trajectory.last_state.reward) + [rw]
        state.detailed_reward = detail
        state.accumulate_reward = sum(state.reward)
        state.task_done = done
        self.trajectory.update("state", state)
        ob = Observation()
        ob.add_text("Current game scene:")
        ob.add_image(img)
        self.trajectory.update("observation", ob)
        self.history_env_states.append(env_state)
        return ob, done

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
                rws.append((obj.accumulate_reward, obj.detailed_reward))
            if tp == "action":
                acs.append(obj.name)

        
        assert len(imgs) == len(rws), (len(imgs), len(rws))

        for i, img in enumerate(imgs):
            I1 = ImageDraw.Draw(img)
            try:
                I1.text((20, 120), "actions: "+ acs[i], fill=(255, 0, 0))
            except:
                pass
            I1.text((20, 150), "frame: "+ str(i), fill=(255, 0, 0))
            I1.text((20, 180), "reward: "+ str(rws[i][0]) , fill=(255, 0, 0))
            for i, di in enumerate(rws[i][1]):
                I1.text((20, 210+i*30), f"reward component {i}: "+ str(di), fill=(255, 0, 0))

        image_arrays = [np.array(img) for img in imgs]  
    
        # Set the duration for each image (seconds per image)  
        fps = 3  # frames per second  
        
        # Create the video clip  
        from moviepy.editor import ImageSequenceClip 
        clip = ImageSequenceClip(image_arrays, fps=fps)  
        
        # Output file path  
        output_video_path = f"{self.tmp_dir}/output_video.mp4"
        
        # Write the video file  
        clip.write_videofile(output_video_path, codec='libx264')



    def get_reward(self, state, action_code, done):
        scaling = 20
        l1 = 0.8  # position moved
        l2 = 1.0  # opponent passed
        l3 = 2.0  # scored
        l4 = 1.0  # stoled
        l5 = 20.0  # pass success
        l6 = 100.0  # shot

        detailed = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        if self.reward_utils is None:
            assert len(self.history_env_states) == 0
            self.reward_utils = {
                "pos_ball_best": state["ball"][0],  # x coordinate
                "last_passed": self.count_pass(state),
                "pass_scale": 1.0,
                "passing_ball": False,
                "prev_ball_owned_player": -1,
                "performed_shot": False,
                "task_done": False
            }
            return 0.0, detailed
        reward = 0.0

        if state["ball_owned_player"] != -1 and state['ball_owned_team'] == 0:
            # position moved
            dt = state["ball"][0]-self.reward_utils["pos_ball_best"]
            r = l1 * max(0, dt)
            reward += r
            detailed[0] = r
            if dt > 0:
                self.reward_utils["pos_ball_best"] = state["ball"][0]
            
            # opponets passed
            cur_passed = self.count_pass(state) 
            r = l2 * (cur_passed - self.reward_utils["last_passed"]) / 11
            reward += r
            detailed[1] = r
            self.reward_utils["last_passed"] = cur_passed

        # scored
        if state["score"][0]>0:
            reward += l3
            detailed[2] = l3
        
        # stole ball
        stoled = False
        if (state['ball_owned_team'] == 1 and
            not self.reward_utils["performed_shot"]):
            stoled = True
            r = l4 * state["steps_left"] / self.NSTEPS - l4
            reward -= r
            detailed[3] = -r
            self.reward_utils["task_done"] = True

        # pass success
        if (self.reward_utils["passing_ball"] and self.reward_utils["prev_ball_owned_player"] != -1 and
            state["ball_owned_player"] != -1 and not stoled and
            state["ball_owned_player"] != self.reward_utils["prev_ball_owned_player"]):
            r = l5 * self.get_pass_clear(state)
            reward += r * self.reward_utils["pass_scale"]
            self.reward_utils["pass_scale"] *= 0.75
            detailed[4] = r
            self.reward_utils["passing_ball"] = False

        if state['ball_owned_player'] != -1:
            self.reward_utils["prev_ball_owned_player"] = state['ball_owned_player']

        if action_code in [9, 10, 11]:
            self.reward_utils["passing_ball"] = True
        
        # shot
        if action_code == 12 and state["ball_owned_player"] != -1 and state["ball_owned_team"] == 0 and not self.reward_utils["performed_shot"]:
            r = l6 * self.get_shot_clear(state) * self.get_shot_distance(state)
            reward += min(r, l3/3)
            detailed[5] = r
            self.reward_utils["performed_shot"] = True
        
        if self.reward_utils["prev_ball_owned_player"] != state['ball_owned_player'] and self.reward_utils["performed_shot"]:
            # this happen when P1 shot ball but not success and catched by p2, then you can continue to shot
            self.reward_utils["performed_shot"] = False
        
        return reward*scaling, [d*scaling for d in detailed]

    def get_shot_distance(self, st):
        dis = 1.0 - st["ball"][0]
        if dis < 0.3:
            return 1.0
        else:
            return max(1.0 - dis / 1.0, 0)

    def get_pass_clear(self, st):
        direction_to_goal = np.array([1.0, 0.0]) - np.array(st["ball"][:2])
        beta = 10
        epsilon = 1

        scores = []
        for player in st["right_team"]:
            direction_to_player = np.array(player) - np.array(st["ball"][:2])
            dis = np.linalg.norm(direction_to_player)
            cos_x = np.dot(direction_to_player, direction_to_goal)/dis/np.linalg.norm(direction_to_goal)
            scores.append(
                dis / (beta * max(cos_x, 0) + epsilon)
            )

        return min(scores)

    def get_shot_clear(self, st):
        goal_points = [np.array([1.0, -0.044]), np.array([1.0, -0.02]), np.array([1.0, 0.0]), np.array([1.0, 0.022]), np.array([1.0, 0.044])]
        ball = np.array(st["ball"][:2])

        dist_best_target = 0
        for target in goal_points:
            trajectory = target - ball
            
            this_target_closest = 1e10
            
            for i in range(100):
                position = ball + (i + 1) / 100.0 * trajectory
                min_d = None
                opp_traj = None
                for p in st['right_team']:
                    d = np.linalg.norm(position - np.array(p))
                    if min_d is None or d < min_d:
                        min_d = d
                        opp_traj = np.array(p)
                dist_traj = np.linalg.norm(position - opp_traj)
                if dist_traj < this_target_closest:
                    this_target_closest = dist_traj
            if this_target_closest > dist_best_target:
                dist_best_target = this_target_closest
        return dist_best_target


    def count_pass(self, st):
        right_teams = st["right_team"]
        return sum([st["ball"][0] > rt[0] for rt in right_teams])
    
    def Evaluator(self, ):
        """Evaluate the cur traj"""
        return self.trajectory.last_state.accumulate_reward, \
                self.trajectory.last_state.info


    @property
    def system_prompt(self, ) -> str:
        '''system rule for this environment, including how to act and observation statements'''
        return """You're going to play a football game. The character you control wears a yellow jersey with a blue name above his head.
Your goal is to attack the goal on the **right side** according to standard soccer rules. It's your teammates who wear the yellow jersey, and the opponents in the other colors.
You'll use text commands to manipulate your character. Here are the action ID and explaination:

- 'action_left', 'action_top_left', 'action_top', 'action_top_right', 'action_right', 'action_bottom_right', 'action_bottom', 'action_bottom_left': Run in the direction corresponding to the action ID's name.
- 'action_long_pass': perform a long pass to the player on your team. Player to pass the ball to is auto-determined based on the movement direction.
- 'action_high_pass': perform a high pass, similar to action_long_pass.
- 'action_short_pass': perform a short pass, similar to action_long_pass.
- 'action_shot': perform a shot, always in the direction of the opponent's goal.
- 'action_sprint', 'action_release_sprint': start and stop sprinting, sticky action. If sprinting, player moves faster, but has worse ball handling.
- 'action_dribble', 'action_release_dribble': start and stop dribbling, sticky action. Player moves slower, but it is harder to take over the ball from him.

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

