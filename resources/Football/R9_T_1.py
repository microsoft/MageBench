
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
    builder.SetBallPosition(0.9813, 0.404)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9587, 0.0093, e_PlayerRole_GK)
    builder.AddPlayer(0.2493, 0.1133, e_PlayerRole_CB)
    builder.AddPlayer(0.576, 0.2987, e_PlayerRole_RB)
    builder.AddPlayer(0.7347, -0.0267, e_PlayerRole_CB)
    builder.AddPlayer(0.752, 0.1227, e_PlayerRole_DM)
    builder.AddPlayer(0.7947, -0.036, e_PlayerRole_DM)
    builder.AddPlayer(0.836, -0.2893, e_PlayerRole_LM)
    builder.AddPlayer(0.8533, 0.1227, e_PlayerRole_DM)
    builder.AddPlayer(0.8987, -0.096, e_PlayerRole_CM)
    builder.AddPlayer(0.9027, 0.0373, e_PlayerRole_CF)
    builder.AddPlayer(0.9867, 0.4093, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.972, -0.0253, e_PlayerRole_GK)
    builder.AddPlayer(-0.8907, -0.056, e_PlayerRole_LB)
    builder.AddPlayer(-0.876, -0.1427, e_PlayerRole_LB)
    builder.AddPlayer(-0.856, 0.2187, e_PlayerRole_RB)
    builder.AddPlayer(-0.852, 0.028, e_PlayerRole_DM)
    builder.AddPlayer(-0.7787, 0.1387, e_PlayerRole_RM)
    builder.AddPlayer(-0.7613, -0.156, e_PlayerRole_LM)
    builder.AddPlayer(-0.7453, -0.0173, e_PlayerRole_DM)
    builder.AddPlayer(-0.6573, -0.076, e_PlayerRole_CM)
    builder.AddPlayer(-0.584, 0.1013, e_PlayerRole_AM)
    builder.AddPlayer(-0.3093, -0.1253, e_PlayerRole_CM)
