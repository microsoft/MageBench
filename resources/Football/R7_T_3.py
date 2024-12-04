
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
    builder.SetBallPosition(-0.7413, 0.26)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.8693, 0.0533, e_PlayerRole_GK)
    builder.AddPlayer(-0.7467, 0.2667, e_PlayerRole_RB)
    builder.AddPlayer(-0.5693, -0.1827, e_PlayerRole_LB)
    builder.AddPlayer(-0.556, 0.1587, e_PlayerRole_RB)
    builder.AddPlayer(-0.3293, -0.2013, e_PlayerRole_LM)
    builder.AddPlayer(-0.3067, 0.3267, e_PlayerRole_RM)
    builder.AddPlayer(-0.248, 0.2187, e_PlayerRole_RM)
    builder.AddPlayer(-0.1853, 0.012, e_PlayerRole_DM)
    builder.AddPlayer(0.088, 0.1293, e_PlayerRole_CF)
    builder.AddPlayer(0.156, -0.0147, e_PlayerRole_CF)
    builder.AddPlayer(0.1827, -0.144, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9587, -0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.1733, -0.0107, e_PlayerRole_CB)
    builder.AddPlayer(-0.152, 0.128, e_PlayerRole_RB)
    builder.AddPlayer(-0.0387, -0.1493, e_PlayerRole_LB)
    builder.AddPlayer(0.0507, 0.1067, e_PlayerRole_RM)
    builder.AddPlayer(0.316, -0.076, e_PlayerRole_DM)
    builder.AddPlayer(0.328, 0.1613, e_PlayerRole_RM)
    builder.AddPlayer(0.408, -0.2653, e_PlayerRole_LM)
    builder.AddPlayer(0.5547, -0.264, e_PlayerRole_CM)
    builder.AddPlayer(0.5733, 0.1467, e_PlayerRole_AM)
    builder.AddPlayer(0.8587, -0.0613, e_PlayerRole_CF)
