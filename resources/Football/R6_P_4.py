
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
    builder.SetBallPosition(0.5187, -0.1547)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9893, 0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.648, 0.1813, e_PlayerRole_RB)
    builder.AddPlayer(-0.6347, -0.092, e_PlayerRole_CB)
    builder.AddPlayer(-0.5107, 0.072, e_PlayerRole_RB)
    builder.AddPlayer(-0.364, 0.224, e_PlayerRole_RM)
    builder.AddPlayer(-0.3627, -0.1387, e_PlayerRole_LM)
    builder.AddPlayer(-0.168, -0.0253, e_PlayerRole_DM)
    builder.AddPlayer(0.1253, -0.252, e_PlayerRole_LM)
    builder.AddPlayer(0.168, 0.04, e_PlayerRole_CF)
    builder.AddPlayer(0.2747, 0.1773, e_PlayerRole_AM)
    builder.AddPlayer(0.5067, -0.1573, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.7533, 0.096, e_PlayerRole_GK)
    builder.AddPlayer(-0.556, -0.0627, e_PlayerRole_LB)
    builder.AddPlayer(-0.4147, -0.2093, e_PlayerRole_LB)
    builder.AddPlayer(-0.308, 0.0147, e_PlayerRole_CB)
    builder.AddPlayer(-0.196, 0.2747, e_PlayerRole_RM)
    builder.AddPlayer(0.1147, 0.0733, e_PlayerRole_DM)
    builder.AddPlayer(0.3027, 0.1933, e_PlayerRole_RM)
    builder.AddPlayer(0.3213, -0.1867, e_PlayerRole_LM)
    builder.AddPlayer(0.484, -0.0387, e_PlayerRole_CF)
    builder.AddPlayer(0.5533, 0.1093, e_PlayerRole_CF)
    builder.AddPlayer(0.5933, -0.1613, e_PlayerRole_CM)
