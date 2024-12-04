
from .football_bot import Player as bot_player
from .WebUI_env import WebUIEnv, WebUIAction
from .sokoban_env import SokobanEnv, SokobanAction
from .football_env import FootballEnv, FootballAction


def get_env(tpy):
    if tpy == "WebUI":
        return WebUIEnv, WebUIAction
    elif tpy == "Sokoban":
        return SokobanEnv, SokobanAction
    elif tpy == "Football":
        return FootballEnv, FootballAction
    
