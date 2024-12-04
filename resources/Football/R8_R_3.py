
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
    builder.SetBallPosition(0.0853, 0.312)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.972, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.4813, -0.0333, e_PlayerRole_CB)
    builder.AddPlayer(-0.408, 0.2187, e_PlayerRole_RB)
    builder.AddPlayer(-0.1693, -0.1213, e_PlayerRole_CB)
    builder.AddPlayer(-0.052, 0.028, e_PlayerRole_DM)
    builder.AddPlayer(0.0747, 0.316, e_PlayerRole_RM)
    builder.AddPlayer(0.1227, -0.04, e_PlayerRole_DM)
    builder.AddPlayer(0.1267, -0.3747, e_PlayerRole_LM)
    builder.AddPlayer(0.18, 0.152, e_PlayerRole_AM)
    builder.AddPlayer(0.404, -0.3773, e_PlayerRole_CM)
    builder.AddPlayer(0.6133, -0.1467, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9653, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.748, -0.2787, e_PlayerRole_LB)
    builder.AddPlayer(-0.6467, 0.1747, e_PlayerRole_RB)
    builder.AddPlayer(-0.512, 0.288, e_PlayerRole_RB)
    builder.AddPlayer(-0.272, -0.176, e_PlayerRole_LM)
    builder.AddPlayer(-0.2693, -0.1, e_PlayerRole_LM)
    builder.AddPlayer(-0.2493, 0.096, e_PlayerRole_DM)
    builder.AddPlayer(-0.228, 0.284, e_PlayerRole_RM)
    builder.AddPlayer(0.0133, 0.0467, e_PlayerRole_CF)
    builder.AddPlayer(0.088, -0.1027, e_PlayerRole_CM)
    builder.AddPlayer(0.3333, 0.0267, e_PlayerRole_CF)
