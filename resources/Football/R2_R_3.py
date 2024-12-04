
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
    builder.SetBallPosition(-0.2333, -0.276)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.964, 0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.5653, 0.156, e_PlayerRole_RB)
    builder.AddPlayer(-0.5493, -0.1387, e_PlayerRole_CB)
    builder.AddPlayer(-0.4907, -0.2293, e_PlayerRole_LB)
    builder.AddPlayer(-0.4347, -0.3227, e_PlayerRole_LM)
    builder.AddPlayer(-0.2653, -0.316, e_PlayerRole_LM)
    builder.AddPlayer(-0.244, 0.0493, e_PlayerRole_RM)
    builder.AddPlayer(-0.24, -0.2733, e_PlayerRole_LM)
    builder.AddPlayer(-0.136, -0.3453, e_PlayerRole_CM)
    builder.AddPlayer(-0.0827, -0.156, e_PlayerRole_CF)
    builder.AddPlayer(-0.0347, 0.04, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.964, 0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.1933, 0.3267, e_PlayerRole_RB)
    builder.AddPlayer(-0.1733, 0.1373, e_PlayerRole_CB)
    builder.AddPlayer(-0.1, -0.012, e_PlayerRole_LB)
    builder.AddPlayer(0.0307, 0.164, e_PlayerRole_DM)
    builder.AddPlayer(0.0813, 0.312, e_PlayerRole_RM)
    builder.AddPlayer(0.196, 0.3933, e_PlayerRole_RM)
    builder.AddPlayer(0.2027, 0.196, e_PlayerRole_DM)
    builder.AddPlayer(0.3427, 0.3293, e_PlayerRole_AM)
    builder.AddPlayer(0.3893, 0.2667, e_PlayerRole_AM)
    builder.AddPlayer(0.5027, 0.076, e_PlayerRole_CM)
