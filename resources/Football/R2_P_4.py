
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
    builder.SetBallPosition(0.0573, -0.2253)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9813, 0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.4747, 0.0453, e_PlayerRole_RB)
    builder.AddPlayer(-0.4253, -0.2053, e_PlayerRole_CB)
    builder.AddPlayer(-0.272, -0.1107, e_PlayerRole_CB)
    builder.AddPlayer(-0.2507, 0.144, e_PlayerRole_RM)
    builder.AddPlayer(-0.188, -0.124, e_PlayerRole_DM)
    builder.AddPlayer(-0.148, -0.34, e_PlayerRole_LM)
    builder.AddPlayer(-0.1347, 0.0013, e_PlayerRole_RM)
    builder.AddPlayer(-0.0693, -0.3987, e_PlayerRole_CM)
    builder.AddPlayer(0.0453, -0.232, e_PlayerRole_CM)
    builder.AddPlayer(0.0573, -0.376, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9853, -0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.7253, 0.132, e_PlayerRole_CB)
    builder.AddPlayer(-0.5373, -0.0893, e_PlayerRole_LB)
    builder.AddPlayer(-0.3333, 0.2813, e_PlayerRole_RB)
    builder.AddPlayer(-0.228, 0.1587, e_PlayerRole_DM)
    builder.AddPlayer(-0.104, 0.38, e_PlayerRole_RM)
    builder.AddPlayer(0.0453, 0.3347, e_PlayerRole_RM)
    builder.AddPlayer(0.0653, 0.012, e_PlayerRole_LM)
    builder.AddPlayer(0.1667, 0.148, e_PlayerRole_CF)
    builder.AddPlayer(0.244, 0.2813, e_PlayerRole_AM)
    builder.AddPlayer(0.4507, -0.0213, e_PlayerRole_CM)
