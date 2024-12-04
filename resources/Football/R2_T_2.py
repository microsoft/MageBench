
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
    builder.SetBallPosition(-0.0773, -0.1707)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.968, 0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.664, -0.1707, e_PlayerRole_CB)
    builder.AddPlayer(-0.4613, 0.044, e_PlayerRole_RB)
    builder.AddPlayer(-0.3467, -0.3787, e_PlayerRole_LB)
    builder.AddPlayer(-0.2933, -0.208, e_PlayerRole_DM)
    builder.AddPlayer(-0.0707, -0.156, e_PlayerRole_DM)
    builder.AddPlayer(-0.0693, -0.356, e_PlayerRole_LM)
    builder.AddPlayer(0.104, -0.276, e_PlayerRole_LM)
    builder.AddPlayer(0.1587, 0.016, e_PlayerRole_AM)
    builder.AddPlayer(0.38, -0.1373, e_PlayerRole_CF)
    builder.AddPlayer(0.5067, -0.304, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9453, 0.0053, e_PlayerRole_GK)
    builder.AddPlayer(-0.68, 0.2533, e_PlayerRole_RB)
    builder.AddPlayer(-0.456, 0.084, e_PlayerRole_CB)
    builder.AddPlayer(-0.3573, -0.2667, e_PlayerRole_LB)
    builder.AddPlayer(-0.2627, -0.0613, e_PlayerRole_LM)
    builder.AddPlayer(-0.1133, 0.3893, e_PlayerRole_RM)
    builder.AddPlayer(-0.076, 0.144, e_PlayerRole_DM)
    builder.AddPlayer(0.116, 0.0613, e_PlayerRole_DM)
    builder.AddPlayer(0.1907, 0.3, e_PlayerRole_AM)
    builder.AddPlayer(0.428, -0.1653, e_PlayerRole_CM)
    builder.AddPlayer(0.552, 0.104, e_PlayerRole_CF)
