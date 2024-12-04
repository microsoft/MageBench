
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
    builder.SetBallPosition(0.0733, -0.3267)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9853, 0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.6853, 0.0613, e_PlayerRole_RB)
    builder.AddPlayer(-0.5613, -0.2187, e_PlayerRole_LB)
    builder.AddPlayer(-0.4307, -0.0213, e_PlayerRole_RB)
    builder.AddPlayer(-0.3733, -0.344, e_PlayerRole_LM)
    builder.AddPlayer(-0.304, 0.1347, e_PlayerRole_RM)
    builder.AddPlayer(-0.1947, -0.3093, e_PlayerRole_LM)
    builder.AddPlayer(-0.1627, -0.156, e_PlayerRole_DM)
    builder.AddPlayer(-0.0587, -0.2507, e_PlayerRole_CM)
    builder.AddPlayer(0.0533, -0.3267, e_PlayerRole_CM)
    builder.AddPlayer(0.108, -0.0813, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.976, -0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.628, 0.356, e_PlayerRole_RB)
    builder.AddPlayer(-0.292, 0.24, e_PlayerRole_RB)
    builder.AddPlayer(-0.2547, 0.032, e_PlayerRole_LB)
    builder.AddPlayer(-0.1053, 0.14, e_PlayerRole_DM)
    builder.AddPlayer(0.0347, 0.256, e_PlayerRole_RM)
    builder.AddPlayer(0.0693, 0.0413, e_PlayerRole_LM)
    builder.AddPlayer(0.128, 0.2933, e_PlayerRole_RM)
    builder.AddPlayer(0.1773, 0.3107, e_PlayerRole_AM)
    builder.AddPlayer(0.312, 0.356, e_PlayerRole_AM)
    builder.AddPlayer(0.336, 0.0413, e_PlayerRole_CM)
