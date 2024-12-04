
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
    builder.SetBallPosition(0.1133, 0.22)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9627, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.536, 0.3067, e_PlayerRole_RB)
    builder.AddPlayer(-0.2773, 0.2187, e_PlayerRole_RB)
    builder.AddPlayer(-0.2187, -0.144, e_PlayerRole_LB)
    builder.AddPlayer(0.0907, -0.3467, e_PlayerRole_LM)
    builder.AddPlayer(0.1147, 0.2293, e_PlayerRole_RM)
    builder.AddPlayer(0.1253, 0.0507, e_PlayerRole_DM)
    builder.AddPlayer(0.308, -0.2053, e_PlayerRole_LM)
    builder.AddPlayer(0.6413, -0.1933, e_PlayerRole_CM)
    builder.AddPlayer(0.7053, -0.0347, e_PlayerRole_CF)
    builder.AddPlayer(0.7253, 0.18, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.976, -0.0, e_PlayerRole_GK)
    builder.AddPlayer(-0.708, -0.164, e_PlayerRole_LB)
    builder.AddPlayer(-0.652, 0.108, e_PlayerRole_RB)
    builder.AddPlayer(-0.5973, 0.2413, e_PlayerRole_RB)
    builder.AddPlayer(-0.3147, -0.1027, e_PlayerRole_DM)
    builder.AddPlayer(-0.244, -0.2627, e_PlayerRole_LM)
    builder.AddPlayer(-0.18, 0.0053, e_PlayerRole_DM)
    builder.AddPlayer(0.0267, 0.108, e_PlayerRole_RM)
    builder.AddPlayer(0.0293, -0.256, e_PlayerRole_CM)
    builder.AddPlayer(0.1307, -0.0773, e_PlayerRole_CF)
    builder.AddPlayer(0.4373, -0.3173, e_PlayerRole_CM)
