
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
    builder.SetBallPosition(-0.688, 0.1467)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9533, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.728, 0.2613, e_PlayerRole_RB)
    builder.AddPlayer(-0.6787, 0.152, e_PlayerRole_RB)
    builder.AddPlayer(-0.608, -0.0307, e_PlayerRole_CB)
    builder.AddPlayer(-0.32, 0.0853, e_PlayerRole_DM)
    builder.AddPlayer(-0.2147, 0.208, e_PlayerRole_RM)
    builder.AddPlayer(-0.18, -0.128, e_PlayerRole_LM)
    builder.AddPlayer(-0.064, 0.2, e_PlayerRole_RM)
    builder.AddPlayer(0.116, 0.104, e_PlayerRole_AM)
    builder.AddPlayer(0.1613, -0.04, e_PlayerRole_CF)
    builder.AddPlayer(0.1973, -0.2427, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9707, -0.0, e_PlayerRole_GK)
    builder.AddPlayer(-0.4453, 0.0707, e_PlayerRole_CB)
    builder.AddPlayer(-0.3947, 0.2493, e_PlayerRole_RB)
    builder.AddPlayer(-0.2573, -0.256, e_PlayerRole_LB)
    builder.AddPlayer(-0.244, -0.072, e_PlayerRole_DM)
    builder.AddPlayer(-0.06, 0.1627, e_PlayerRole_RM)
    builder.AddPlayer(0.148, -0.24, e_PlayerRole_LM)
    builder.AddPlayer(0.2933, -0.124, e_PlayerRole_LM)
    builder.AddPlayer(0.3213, 0.0587, e_PlayerRole_CF)
    builder.AddPlayer(0.5333, -0.1013, e_PlayerRole_CM)
    builder.AddPlayer(0.652, -0.2173, e_PlayerRole_CM)
