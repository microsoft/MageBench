
import gfootball_engine as libgame
e_PlayerRole_GK = libgame.e_PlayerRole.e_PlayerRole_GK
e_PlayerRole_CB = libgame.e_PlayerRole.e_PlayerRole_CB
e_PlayerRole_LB = libgame.e_PlayerRole.e_PlayerRole_LB
e_PlayerRole_RB = libgame.e_PlayerRole.e_PlayerRole_RB
e_PlayerRole_DM = libgame.e_PlayerRole.e_PlayerRole_DM
e_PlayerRole_CM = libgame.e_PlayerRole.e_PlayerRole_CM
e_PlayerRole_LM = libgame.e_PlayerRole.e_PlayerRole_LM
e_PlayerRole_RM = libgame.e_PlayerRole.e_PlayerRole_RM
e_PlayerRole_AM = libgame.e_PlayerRole.e_PlayerRole_AM
e_PlayerRole_CF = libgame.e_PlayerRole.e_PlayerRole_CF
Team = libgame.e_Team

def build_scenario(builder):
    builder.config().game_duration = 400
    builder.config().deterministic = False
    builder.config().offsides = False
    builder.config().end_episode_on_score = True
    builder.config().end_episode_on_out_of_play = True
    builder.config().end_episode_on_possession_change = True
    builder.config().right_team_difficulty = 0.0
    builder.config().left_team_difficulty = 1.0
    builder.SetBallPosition(-0.108, -0.3387)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9827, 0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.836, 0.104, e_PlayerRole_RB)
    builder.AddPlayer(-0.5573, -0.1053, e_PlayerRole_CB)
    builder.AddPlayer(-0.5, -0.1627, e_PlayerRole_CB)
    builder.AddPlayer(-0.364, -0.096, e_PlayerRole_DM)
    builder.AddPlayer(-0.3533, -0.2213, e_PlayerRole_LM)
    builder.AddPlayer(-0.34, -0.0267, e_PlayerRole_DM)
    builder.AddPlayer(-0.2373, -0.0453, e_PlayerRole_DM)
    builder.AddPlayer(-0.188, -0.1973, e_PlayerRole_CM)
    builder.AddPlayer(-0.1333, -0.3387, e_PlayerRole_CM)
    builder.AddPlayer(-0.0373, 0.1627, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9667, -0.0107, e_PlayerRole_GK)
    builder.AddPlayer(-0.5947, 0.176, e_PlayerRole_CB)
    builder.AddPlayer(-0.3747, 0.0093, e_PlayerRole_LB)
    builder.AddPlayer(-0.216, -0.1013, e_PlayerRole_LB)
    builder.AddPlayer(-0.056, 0.3667, e_PlayerRole_RM)
    builder.AddPlayer(0.056, 0.0227, e_PlayerRole_LM)
    builder.AddPlayer(0.1707, 0.248, e_PlayerRole_RM)
    builder.AddPlayer(0.204, 0.1347, e_PlayerRole_DM)
    builder.AddPlayer(0.2987, 0.272, e_PlayerRole_AM)
    builder.AddPlayer(0.324, 0.1573, e_PlayerRole_CF)
    builder.AddPlayer(0.4693, 0.2507, e_PlayerRole_AM)
