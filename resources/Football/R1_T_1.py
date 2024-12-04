
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
    builder.SetBallPosition(-0.86, -0.1707)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.98, 0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.868, -0.1613, e_PlayerRole_CB)
    builder.AddPlayer(-0.8187, -0.356, e_PlayerRole_LB)
    builder.AddPlayer(-0.684, -0.2653, e_PlayerRole_LB)
    builder.AddPlayer(-0.608, 0.184, e_PlayerRole_RM)
    builder.AddPlayer(-0.5947, -0.34, e_PlayerRole_LM)
    builder.AddPlayer(-0.4333, -0.1987, e_PlayerRole_LM)
    builder.AddPlayer(-0.3053, 0.0347, e_PlayerRole_RM)
    builder.AddPlayer(-0.1573, -0.112, e_PlayerRole_CF)
    builder.AddPlayer(-0.152, 0.1827, e_PlayerRole_AM)
    builder.AddPlayer(0.108, -0.3333, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9747, -0.0053, e_PlayerRole_GK)
    builder.AddPlayer(-0.444, 0.3, e_PlayerRole_RB)
    builder.AddPlayer(-0.3347, -0.1413, e_PlayerRole_LB)
    builder.AddPlayer(-0.2253, 0.0507, e_PlayerRole_CB)
    builder.AddPlayer(0.092, 0.124, e_PlayerRole_DM)
    builder.AddPlayer(0.2667, -0.0453, e_PlayerRole_LM)
    builder.AddPlayer(0.2933, -0.2, e_PlayerRole_LM)
    builder.AddPlayer(0.4547, 0.2987, e_PlayerRole_RM)
    builder.AddPlayer(0.632, 0.148, e_PlayerRole_AM)
    builder.AddPlayer(0.668, -0.1333, e_PlayerRole_CM)
    builder.AddPlayer(0.7427, 0.244, e_PlayerRole_AM)
