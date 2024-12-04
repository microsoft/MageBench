
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
    builder.SetBallPosition(0.6613, -0.0773)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9773, 0.0053, e_PlayerRole_GK)
    builder.AddPlayer(-0.7453, 0.1147, e_PlayerRole_CB)
    builder.AddPlayer(-0.6747, -0.0933, e_PlayerRole_LB)
    builder.AddPlayer(-0.552, 0.3773, e_PlayerRole_RB)
    builder.AddPlayer(-0.4413, 0.0813, e_PlayerRole_DM)
    builder.AddPlayer(-0.412, -0.084, e_PlayerRole_DM)
    builder.AddPlayer(-0.36, -0.328, e_PlayerRole_LM)
    builder.AddPlayer(0.24, 0.076, e_PlayerRole_DM)
    builder.AddPlayer(0.2813, -0.2013, e_PlayerRole_CM)
    builder.AddPlayer(0.648, -0.072, e_PlayerRole_CF)
    builder.AddPlayer(0.9573, -0.0067, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.928, 0.016, e_PlayerRole_GK)
    builder.AddPlayer(-0.544, -0.0267, e_PlayerRole_CB)
    builder.AddPlayer(-0.2613, 0.2813, e_PlayerRole_RB)
    builder.AddPlayer(-0.188, -0.06, e_PlayerRole_CB)
    builder.AddPlayer(0.1667, -0.1613, e_PlayerRole_LM)
    builder.AddPlayer(0.2867, 0.28, e_PlayerRole_RM)
    builder.AddPlayer(0.356, 0.084, e_PlayerRole_DM)
    builder.AddPlayer(0.492, -0.096, e_PlayerRole_DM)
    builder.AddPlayer(0.5333, 0.0893, e_PlayerRole_AM)
    builder.AddPlayer(0.5907, -0.304, e_PlayerRole_CM)
    builder.AddPlayer(0.6693, -0.072, e_PlayerRole_CF)
