
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
    builder.SetBallPosition(-0.1107, -0.056)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9493, 0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.728, -0.044, e_PlayerRole_CB)
    builder.AddPlayer(-0.5947, 0.1013, e_PlayerRole_RB)
    builder.AddPlayer(-0.5293, -0.1693, e_PlayerRole_LB)
    builder.AddPlayer(-0.3627, 0.1533, e_PlayerRole_RM)
    builder.AddPlayer(-0.124, -0.068, e_PlayerRole_DM)
    builder.AddPlayer(0.044, 0.076, e_PlayerRole_RM)
    builder.AddPlayer(0.072, -0.1067, e_PlayerRole_LM)
    builder.AddPlayer(0.2413, 0.108, e_PlayerRole_AM)
    builder.AddPlayer(0.244, -0.0107, e_PlayerRole_CF)
    builder.AddPlayer(0.2853, -0.1867, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9773, -0.0053, e_PlayerRole_GK)
    builder.AddPlayer(-0.62, -0.1333, e_PlayerRole_LB)
    builder.AddPlayer(-0.328, -0.2013, e_PlayerRole_LB)
    builder.AddPlayer(-0.2693, 0.1013, e_PlayerRole_RB)
    builder.AddPlayer(-0.088, 0.0213, e_PlayerRole_DM)
    builder.AddPlayer(-0.0467, 0.2453, e_PlayerRole_RM)
    builder.AddPlayer(0.0147, 0.0307, e_PlayerRole_DM)
    builder.AddPlayer(0.2533, -0.2453, e_PlayerRole_LM)
    builder.AddPlayer(0.4253, 0.1173, e_PlayerRole_AM)
    builder.AddPlayer(0.4627, -0.124, e_PlayerRole_CM)
    builder.AddPlayer(0.5973, 0.0253, e_PlayerRole_CF)
