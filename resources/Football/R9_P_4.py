
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
    builder.SetBallPosition(0.9787, 0.1493)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9867, 0.0027, e_PlayerRole_GK)
    builder.AddPlayer(0.3747, -0.012, e_PlayerRole_CB)
    builder.AddPlayer(0.4387, 0.2053, e_PlayerRole_RB)
    builder.AddPlayer(0.5613, 0.3013, e_PlayerRole_RB)
    builder.AddPlayer(0.572, 0.1293, e_PlayerRole_RM)
    builder.AddPlayer(0.656, -0.1707, e_PlayerRole_LM)
    builder.AddPlayer(0.7867, 0.3173, e_PlayerRole_RM)
    builder.AddPlayer(0.8053, -0.3293, e_PlayerRole_LM)
    builder.AddPlayer(0.8173, 0.0387, e_PlayerRole_CF)
    builder.AddPlayer(0.8667, -0.1427, e_PlayerRole_CM)
    builder.AddPlayer(0.9907, 0.156, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9893, 0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.984, -0.2747, e_PlayerRole_LB)
    builder.AddPlayer(-0.888, 0.108, e_PlayerRole_RB)
    builder.AddPlayer(-0.8467, -0.0493, e_PlayerRole_CB)
    builder.AddPlayer(-0.828, 0.2907, e_PlayerRole_RM)
    builder.AddPlayer(-0.8053, -0.2707, e_PlayerRole_LM)
    builder.AddPlayer(-0.688, 0.128, e_PlayerRole_RM)
    builder.AddPlayer(-0.6547, -0.164, e_PlayerRole_LM)
    builder.AddPlayer(-0.6213, -0.3187, e_PlayerRole_CM)
    builder.AddPlayer(-0.552, 0.3, e_PlayerRole_AM)
    builder.AddPlayer(-0.444, -0.1067, e_PlayerRole_CF)
