
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
    builder.SetBallPosition(-0.5667, -0.268)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.944, -0.0053, e_PlayerRole_GK)
    builder.AddPlayer(-0.872, -0.1427, e_PlayerRole_LB)
    builder.AddPlayer(-0.8173, -0.3213, e_PlayerRole_LB)
    builder.AddPlayer(-0.644, -0.0587, e_PlayerRole_CB)
    builder.AddPlayer(-0.5853, -0.2773, e_PlayerRole_LM)
    builder.AddPlayer(-0.5067, 0.28, e_PlayerRole_RM)
    builder.AddPlayer(-0.432, -0.0707, e_PlayerRole_DM)
    builder.AddPlayer(-0.432, -0.2067, e_PlayerRole_LM)
    builder.AddPlayer(-0.38, -0.34, e_PlayerRole_CM)
    builder.AddPlayer(-0.2093, -0.0973, e_PlayerRole_CF)
    builder.AddPlayer(-0.1893, 0.188, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.972, -0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.4347, -0.052, e_PlayerRole_CB)
    builder.AddPlayer(0.0493, 0.0493, e_PlayerRole_CB)
    builder.AddPlayer(0.08, -0.2587, e_PlayerRole_LB)
    builder.AddPlayer(0.2747, -0.004, e_PlayerRole_DM)
    builder.AddPlayer(0.292, 0.208, e_PlayerRole_RM)
    builder.AddPlayer(0.4213, -0.3613, e_PlayerRole_LM)
    builder.AddPlayer(0.4787, 0.3187, e_PlayerRole_RM)
    builder.AddPlayer(0.48, -0.1427, e_PlayerRole_CM)
    builder.AddPlayer(0.4813, 0.1173, e_PlayerRole_AM)
    builder.AddPlayer(0.7787, 0.2947, e_PlayerRole_AM)
