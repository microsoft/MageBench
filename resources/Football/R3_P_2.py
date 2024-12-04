
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
    builder.SetBallPosition(0.8507, -0.304)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9853, -0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.5893, 0.1213, e_PlayerRole_RB)
    builder.AddPlayer(-0.18, -0.104, e_PlayerRole_CB)
    builder.AddPlayer(0.296, 0.2173, e_PlayerRole_RB)
    builder.AddPlayer(0.3, -0.2213, e_PlayerRole_LM)
    builder.AddPlayer(0.464, 0.0307, e_PlayerRole_DM)
    builder.AddPlayer(0.636, -0.384, e_PlayerRole_LM)
    builder.AddPlayer(0.6693, 0.0707, e_PlayerRole_DM)
    builder.AddPlayer(0.6733, -0.0467, e_PlayerRole_CF)
    builder.AddPlayer(0.74, 0.3347, e_PlayerRole_AM)
    builder.AddPlayer(0.848, -0.32, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9893, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.8747, -0.2653, e_PlayerRole_LB)
    builder.AddPlayer(-0.8267, 0.188, e_PlayerRole_RB)
    builder.AddPlayer(-0.7653, -0.0253, e_PlayerRole_CB)
    builder.AddPlayer(-0.756, -0.2773, e_PlayerRole_LM)
    builder.AddPlayer(-0.692, 0.0493, e_PlayerRole_DM)
    builder.AddPlayer(-0.656, 0.3773, e_PlayerRole_RM)
    builder.AddPlayer(-0.5853, -0.148, e_PlayerRole_LM)
    builder.AddPlayer(-0.4933, 0.0013, e_PlayerRole_CF)
    builder.AddPlayer(-0.3267, 0.2293, e_PlayerRole_AM)
    builder.AddPlayer(-0.3187, -0.1867, e_PlayerRole_CM)
