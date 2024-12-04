# custom_config.py  
  
# Import the necessary modules and classes  
import importlib.util  
import sys  
import os  
import tempfile  
import copy  
import gfootball_engine as libgame  
from gfootball.env.config import Config as BaseConfig  
from gfootball.env.scenario_builder import Scenario as BaseScenario  
  
  
class Scenario(BaseScenario):  
    def __init__(self, config, path):  
        # Game config controls C++ engine and is derived from the main config.  
        self._scenario_cfg = libgame.ScenarioConfig.make()  
        self._config = config  
        self._active_team = libgame.e_Team.e_Left  
        scenario = None  
        try:  
            file_path = path  
            module_name = 'scenario'  # 模块名可以随意命名  
            spec = importlib.util.spec_from_file_location(module_name, file_path)  
            scenario = importlib.util.module_from_spec(spec)  
            spec.loader.exec_module(scenario)  
            sys.modules[module_name] = scenario  
        except ImportError as e:  
            sys.exit(1)  
        scenario.build_scenario(self)  
        self.SetTeam(libgame.e_Team.e_Left)  
        self._FakePlayersForEmptyTeam(self._scenario_cfg.left_team)  
        self.SetTeam(libgame.e_Team.e_Right)  
        self._FakePlayersForEmptyTeam(self._scenario_cfg.right_team)  
        self._BuildScenarioConfig()  
  
class Config(BaseConfig):  
    def __init__(self, values=None, path=None):  
        self._values = {  
            'action_set': 'default',  
            'custom_display_stats': None,  
            'display_game_stats': True,  
            'dump_full_episodes': False,  
            'dump_scores': False,  
            'players': ['agent:left_players=1'],  
            'level': '11_vs_11_stochastic',  
            'physics_steps_per_frame': 10,  
            'render_resolution_x': 1280,  
            'real_time': False,  
            'tracesdir': os.path.join(tempfile.gettempdir(), 'dumps'),  
            'video_format': 'avi',  
            'video_quality_level': 0,  # 0 - low, 1 - medium, 2 - high  
            'write_video': False  
        }  
        self._values['render_resolution_y'] = int(0.5625 * self._values['render_resolution_x'])  
        if values:  
            self._values.update(values)  
        self._scenario_values = {}  
        if path:  
            self.NewScenario(path)
        else:
            self.NewScenario(values['level'])
      
    def NewScenario(self, path=None, inc=1):  
        if 'episode_number' not in self._values:  
            self._values['episode_number'] = 0  
        self._values['episode_number'] += inc  
        self._scenario_values = {}  
        if path:
            self._scenario_cfg = Scenario(self, path).ScenarioConfig()  
        else:
            self._scenario_cfg = Scenario(self, self._values['level']).ScenarioConfig()  
