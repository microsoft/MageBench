
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
    builder.SetBallPosition(-0.3413, -0.312)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.936, 0.0093, e_PlayerRole_GK)
    builder.AddPlayer(-0.4813, 0.2307, e_PlayerRole_RB)
    builder.AddPlayer(-0.3587, -0.2, e_PlayerRole_LB)
    builder.AddPlayer(-0.3507, -0.312, e_PlayerRole_LB)
    builder.AddPlayer(-0.348, -0.0787, e_PlayerRole_DM)
    builder.AddPlayer(-0.2453, 0.3, e_PlayerRole_RM)
    builder.AddPlayer(-0.0893, -0.312, e_PlayerRole_LM)
    builder.AddPlayer(-0.0613, -0.396, e_PlayerRole_LM)
    builder.AddPlayer(-0.0573, 0.124, e_PlayerRole_AM)
    builder.AddPlayer(0.1267, -0.0493, e_PlayerRole_CF)
    builder.AddPlayer(0.1693, -0.2293, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9547, -0.0, e_PlayerRole_GK)
    builder.AddPlayer(-0.2907, 0.224, e_PlayerRole_RB)
    builder.AddPlayer(-0.272, 0.0173, e_PlayerRole_CB)
    builder.AddPlayer(-0.2173, -0.2053, e_PlayerRole_LB)
    builder.AddPlayer(0.0107, 0.32, e_PlayerRole_RM)
    builder.AddPlayer(0.048, 0.156, e_PlayerRole_DM)
    builder.AddPlayer(0.1707, 0.2493, e_PlayerRole_RM)
    builder.AddPlayer(0.228, -0.204, e_PlayerRole_LM)
    builder.AddPlayer(0.2347, 0.3613, e_PlayerRole_AM)
    builder.AddPlayer(0.4213, -0.028, e_PlayerRole_CM)
    builder.AddPlayer(0.4253, 0.2507, e_PlayerRole_AM)
