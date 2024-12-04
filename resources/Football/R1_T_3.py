
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
    builder.SetBallPosition(-0.7787, -0.1613)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9107, -0.0813, e_PlayerRole_GK)
    builder.AddPlayer(-0.8933, -0.2867, e_PlayerRole_LB)
    builder.AddPlayer(-0.7853, 0.0747, e_PlayerRole_RB)
    builder.AddPlayer(-0.7667, -0.1707, e_PlayerRole_CB)
    builder.AddPlayer(-0.5853, -0.3707, e_PlayerRole_LM)
    builder.AddPlayer(-0.496, -0.084, e_PlayerRole_DM)
    builder.AddPlayer(-0.272, -0.2613, e_PlayerRole_LM)
    builder.AddPlayer(-0.1973, 0.1, e_PlayerRole_RM)
    builder.AddPlayer(-0.0813, -0.0253, e_PlayerRole_CF)
    builder.AddPlayer(0.1893, -0.2053, e_PlayerRole_CM)
    builder.AddPlayer(0.2293, 0.2093, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.96, 0.0147, e_PlayerRole_GK)
    builder.AddPlayer(-0.3133, 0.1893, e_PlayerRole_RB)
    builder.AddPlayer(-0.2853, -0.236, e_PlayerRole_LB)
    builder.AddPlayer(-0.1027, -0.276, e_PlayerRole_LB)
    builder.AddPlayer(-0.1013, 0.2907, e_PlayerRole_RM)
    builder.AddPlayer(0.036, 0.0067, e_PlayerRole_DM)
    builder.AddPlayer(0.108, -0.1893, e_PlayerRole_LM)
    builder.AddPlayer(0.2093, 0.2147, e_PlayerRole_RM)
    builder.AddPlayer(0.6133, 0.148, e_PlayerRole_AM)
    builder.AddPlayer(0.652, 0.2733, e_PlayerRole_AM)
    builder.AddPlayer(0.8467, -0.0413, e_PlayerRole_CF)
