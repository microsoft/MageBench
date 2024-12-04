from typing import List


class Action(object):
    """A possible action for the model"""

    def __init__(self):
        self.text_identifier = ""

    def act(self, ): # writing the acting function here or in the AgentEnvironment
        pass

    @property
    def help(self, ):
        return "a guild for how to use this actions class."
    @property
    def info(self, ):
        assert False
        pass



class Observation(object):
    """Feeback to the model"""
    def __init__(self):
        self.multi_modality_message = []  # OAI format, except that image will be Image.Image format
    def add_text(self, text):
        self.multi_modality_message.append(
            {
                "type": "text",
                "text": text
            }
        )
    def add_image(self, img):
        self.multi_modality_message.append(
            {
                "type": "image_url",
                "image_url": img
            }
        )

    @property
    def is_empty(self, ):
        return len(self.multi_modality_message) == 0
    
    @property
    def info(self, ):
        return self.multi_modality_message

class State(object):
    """A current state for a environment"""

    @property
    def info(self, ):
        assert False
        pass


class EnvTraj(object):
    """EnvTraj here is a trajectory including all history state, actions and observation"""
    def __init__(self):
        self.traj = list()

    def update(self, type, obj):
        assert type in ["state", "action", "observation"]
        self.traj.append((type, obj))
    
    @property
    def last_state(self) -> State:
        for obj in self.traj[::-1]:
            if obj[0] == "state":
                return obj[1]
    
    @property
    def last_observation(self) -> Observation:
        for obj in self.traj[::-1]:
            if obj[0] == "observation":
                return obj[1]

class AgentEnvironment(object):
    def __init__(self, init_traj: EnvTraj):
        self.trajectory = init_traj
        self.history_trojectory = []
        assert isinstance(self.trajectory.last_state, State), "initial state must be provided"

    def get_init_observation(self, ):
        ob = self.trajectory.traj[-1]
        return ob[1]
    
    def _render(self, ) -> Observation:
        """render next observation according to the envtraj"""
    
    def Render(self, ) -> Observation:
        """render next observation according to the envtraj, and add to traj"""
        ob = self._render()
        self.trajectory.update("observation", ob)
        return ob
    
    def take_action(self, act: Action):
        """take a action"""
        self.trajectory.update("action", act)
        state = self.update_state(act)
        self.trajectory.update("state", state)
        ob = self.Render()
        return state, ob
    
    def update_state(self, ) -> State:
        """update and return the state"""
        pass

    def Evaluator(self, ):
        """Evaluate the cur traj"""
        pass

    @property
    def system_prompt(self, ) -> str:
        '''system rule for this environment, including how to act and observation statements'''
        return "" 
    
    @property
    def task_prompt(self, ) -> str:
        '''task description for this environment, for tasks that contain special requirements'''
        return None

    @property
    def valid_actions(self, state = None) -> List[Action]:
        pass
    
    @property
    def action_id(self, ):
        return len(list(filter(lambda x: x[0]=="action", self.trajectory.traj)))
