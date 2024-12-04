
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
    builder.SetBallPosition(0.9187, 0.2693)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9853, 0.0, e_PlayerRole_GK)
    builder.AddPlayer(0.1453, 0.1053, e_PlayerRole_CB)
    builder.AddPlayer(0.256, 0.1613, e_PlayerRole_RB)
    builder.AddPlayer(0.2893, -0.136, e_PlayerRole_LB)
    builder.AddPlayer(0.352, -0.2507, e_PlayerRole_LM)
    builder.AddPlayer(0.428, 0.1507, e_PlayerRole_RM)
    builder.AddPlayer(0.5827, 0.352, e_PlayerRole_RM)
    builder.AddPlayer(0.596, -0.1413, e_PlayerRole_LM)
    builder.AddPlayer(0.7387, -0.3773, e_PlayerRole_CM)
    builder.AddPlayer(0.8133, -0.032, e_PlayerRole_CF)
    builder.AddPlayer(0.9213, 0.2813, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9773, -0.0147, e_PlayerRole_GK)
    builder.AddPlayer(-0.9347, -0.108, e_PlayerRole_CB)
    builder.AddPlayer(-0.8787, 0.1893, e_PlayerRole_RB)
    builder.AddPlayer(-0.832, 0.0013, e_PlayerRole_CB)
    builder.AddPlayer(-0.7907, 0.3107, e_PlayerRole_RM)
    builder.AddPlayer(-0.6467, -0.0493, e_PlayerRole_DM)
    builder.AddPlayer(-0.6253, 0.112, e_PlayerRole_RM)
    builder.AddPlayer(-0.6147, -0.3467, e_PlayerRole_LM)
    builder.AddPlayer(-0.5627, 0.2787, e_PlayerRole_AM)
    builder.AddPlayer(-0.4933, -0.1613, e_PlayerRole_CM)
    builder.AddPlayer(-0.34, 0.0867, e_PlayerRole_CF)
