
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
    builder.SetBallPosition(-0.0253, 0.0213)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9867, 0.0053, e_PlayerRole_GK)
    builder.AddPlayer(-0.8173, 0.0893, e_PlayerRole_RB)
    builder.AddPlayer(-0.8133, 0.0053, e_PlayerRole_CB)
    builder.AddPlayer(-0.8067, 0.1747, e_PlayerRole_RM)
    builder.AddPlayer(-0.3267, 0.1307, e_PlayerRole_RM)
    builder.AddPlayer(-0.1133, -0.0907, e_PlayerRole_LM)
    builder.AddPlayer(-0.0387, 0.02, e_PlayerRole_CF)
    builder.AddPlayer(0.136, -0.1333, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9853, 0.0053, e_PlayerRole_GK)
    builder.AddPlayer(-0.7733, 0.1213, e_PlayerRole_RB)
    builder.AddPlayer(-0.464, 0.0173, e_PlayerRole_CB)
    builder.AddPlayer(-0.3747, -0.096, e_PlayerRole_LB)
    builder.AddPlayer(-0.1547, 0.1467, e_PlayerRole_RM)
    builder.AddPlayer(-0.124, 0.1187, e_PlayerRole_RM)
    builder.AddPlayer(0.1053, 0.088, e_PlayerRole_RM)
    builder.AddPlayer(0.3053, -0.1253, e_PlayerRole_CM)
    builder.AddPlayer(0.5853, -0.0293, e_PlayerRole_CF)
    builder.AddPlayer(0.588, -0.0947, e_PlayerRole_CM)
