
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
    builder.SetBallPosition(0.6827, 0.1467)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9893, 0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.1093, -0.0627, e_PlayerRole_LB)
    builder.AddPlayer(0.1227, 0.0747, e_PlayerRole_CB)
    builder.AddPlayer(0.34, -0.108, e_PlayerRole_LB)
    builder.AddPlayer(0.3907, 0.2053, e_PlayerRole_RM)
    builder.AddPlayer(0.456, 0.0307, e_PlayerRole_DM)
    builder.AddPlayer(0.5893, 0.2453, e_PlayerRole_RM)
    builder.AddPlayer(0.624, 0.3307, e_PlayerRole_RM)
    builder.AddPlayer(0.6413, -0.18, e_PlayerRole_CM)
    builder.AddPlayer(0.668, 0.152, e_PlayerRole_CF)
    builder.AddPlayer(0.7747, 0.2867, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9867, -0.0, e_PlayerRole_GK)
    builder.AddPlayer(-0.8307, -0.1107, e_PlayerRole_CB)
    builder.AddPlayer(-0.78, 0.0347, e_PlayerRole_CB)
    builder.AddPlayer(-0.7573, -0.248, e_PlayerRole_LB)
    builder.AddPlayer(-0.7333, 0.236, e_PlayerRole_RM)
    builder.AddPlayer(-0.6467, 0.144, e_PlayerRole_RM)
    builder.AddPlayer(-0.62, -0.216, e_PlayerRole_LM)
    builder.AddPlayer(-0.6147, -0.2933, e_PlayerRole_LM)
    builder.AddPlayer(-0.5173, -0.0533, e_PlayerRole_CF)
    builder.AddPlayer(-0.44, -0.1813, e_PlayerRole_CM)
    builder.AddPlayer(-0.4253, 0.064, e_PlayerRole_AM)
