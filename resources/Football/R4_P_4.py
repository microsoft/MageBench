
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
    builder.SetBallPosition(-0.764, 0.0627)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.78, 0.056, e_PlayerRole_GK)
    builder.AddPlayer(-0.5347, -0.1227, e_PlayerRole_LB)
    builder.AddPlayer(-0.488, -0.12, e_PlayerRole_LB)
    builder.AddPlayer(-0.436, 0.172, e_PlayerRole_RB)
    builder.AddPlayer(0.1013, -0.036, e_PlayerRole_DM)
    builder.AddPlayer(0.236, -0.2147, e_PlayerRole_LM)
    builder.AddPlayer(0.2573, -0.0893, e_PlayerRole_DM)
    builder.AddPlayer(0.348, -0.2573, e_PlayerRole_LM)
    builder.AddPlayer(0.376, 0.0693, e_PlayerRole_AM)
    builder.AddPlayer(0.496, -0.1467, e_PlayerRole_CM)
    builder.AddPlayer(0.5227, -0.048, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9827, 0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.5053, -0.0867, e_PlayerRole_LB)
    builder.AddPlayer(-0.384, 0.0093, e_PlayerRole_CB)
    builder.AddPlayer(-0.3693, 0.1693, e_PlayerRole_RB)
    builder.AddPlayer(-0.2813, -0.1547, e_PlayerRole_LM)
    builder.AddPlayer(-0.256, 0.0427, e_PlayerRole_DM)
    builder.AddPlayer(-0.2493, 0.2533, e_PlayerRole_RM)
    builder.AddPlayer(-0.1653, 0.1827, e_PlayerRole_RM)
    builder.AddPlayer(0.296, 0.0027, e_PlayerRole_CF)
    builder.AddPlayer(0.4667, -0.1493, e_PlayerRole_CM)
    builder.AddPlayer(0.544, 0.1013, e_PlayerRole_CF)
