
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
    builder.SetBallPosition(-0.8987, -0.004)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9093, 0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.8467, 0.2573, e_PlayerRole_RB)
    builder.AddPlayer(-0.808, -0.3107, e_PlayerRole_LB)
    builder.AddPlayer(-0.752, 0.1453, e_PlayerRole_RB)
    builder.AddPlayer(-0.74, -0.1107, e_PlayerRole_DM)
    builder.AddPlayer(-0.6293, -0.0187, e_PlayerRole_DM)
    builder.AddPlayer(-0.4067, 0.0893, e_PlayerRole_RM)
    builder.AddPlayer(-0.404, -0.2307, e_PlayerRole_LM)
    builder.AddPlayer(-0.396, 0.228, e_PlayerRole_AM)
    builder.AddPlayer(-0.212, -0.072, e_PlayerRole_CF)
    builder.AddPlayer(-0.1093, 0.148, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.968, 0.016, e_PlayerRole_GK)
    builder.AddPlayer(-0.2227, -0.1467, e_PlayerRole_LB)
    builder.AddPlayer(-0.072, 0.0907, e_PlayerRole_CB)
    builder.AddPlayer(0.0707, 0.2067, e_PlayerRole_RB)
    builder.AddPlayer(0.152, -0.14, e_PlayerRole_LM)
    builder.AddPlayer(0.2267, 0.0467, e_PlayerRole_DM)
    builder.AddPlayer(0.288, 0.22, e_PlayerRole_RM)
    builder.AddPlayer(0.3213, -0.112, e_PlayerRole_LM)
    builder.AddPlayer(0.556, 0.028, e_PlayerRole_CF)
    builder.AddPlayer(0.6627, -0.084, e_PlayerRole_CM)
    builder.AddPlayer(0.8187, 0.1213, e_PlayerRole_AM)
