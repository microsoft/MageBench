
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
    builder.SetBallPosition(0.064, 0.3693)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9773, 0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.456, 0.1693, e_PlayerRole_RB)
    builder.AddPlayer(-0.3147, 0.1493, e_PlayerRole_RB)
    builder.AddPlayer(-0.2507, -0.14, e_PlayerRole_LB)
    builder.AddPlayer(-0.2373, 0.0907, e_PlayerRole_DM)
    builder.AddPlayer(-0.22, 0.336, e_PlayerRole_RM)
    builder.AddPlayer(-0.1013, -0.012, e_PlayerRole_DM)
    builder.AddPlayer(-0.0813, -0.3173, e_PlayerRole_LM)
    builder.AddPlayer(0.0253, 0.1773, e_PlayerRole_AM)
    builder.AddPlayer(0.0467, 0.3667, e_PlayerRole_AM)
    builder.AddPlayer(0.0493, -0.0973, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.98, 0.0053, e_PlayerRole_GK)
    builder.AddPlayer(-0.5, -0.38, e_PlayerRole_LB)
    builder.AddPlayer(-0.3067, -0.292, e_PlayerRole_LB)
    builder.AddPlayer(-0.1107, 0.0227, e_PlayerRole_RB)
    builder.AddPlayer(-0.044, -0.216, e_PlayerRole_DM)
    builder.AddPlayer(0.0613, -0.1973, e_PlayerRole_DM)
    builder.AddPlayer(0.0907, -0.0587, e_PlayerRole_DM)
    builder.AddPlayer(0.1427, -0.3293, e_PlayerRole_LM)
    builder.AddPlayer(0.208, 0.1093, e_PlayerRole_AM)
    builder.AddPlayer(0.2653, -0.1733, e_PlayerRole_CF)
    builder.AddPlayer(0.552, -0.14, e_PlayerRole_CF)
