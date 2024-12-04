
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
    builder.SetBallPosition(-0.9467, 0.0333)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9613, 0.0187, e_PlayerRole_GK)
    builder.AddPlayer(-0.8907, 0.204, e_PlayerRole_RB)
    builder.AddPlayer(-0.7267, -0.3133, e_PlayerRole_LB)
    builder.AddPlayer(-0.6947, 0.2773, e_PlayerRole_RB)
    builder.AddPlayer(-0.636, 0.14, e_PlayerRole_RM)
    builder.AddPlayer(-0.6027, -0.2267, e_PlayerRole_LM)
    builder.AddPlayer(-0.544, -0.1107, e_PlayerRole_DM)
    builder.AddPlayer(-0.204, 0.3027, e_PlayerRole_RM)
    builder.AddPlayer(-0.1893, 0.1667, e_PlayerRole_AM)
    builder.AddPlayer(-0.1613, -0.0987, e_PlayerRole_CF)
    builder.AddPlayer(-0.1347, -0.3307, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9453, -0.0053, e_PlayerRole_GK)
    builder.AddPlayer(-0.4747, 0.04, e_PlayerRole_CB)
    builder.AddPlayer(0.0213, 0.0453, e_PlayerRole_CB)
    builder.AddPlayer(0.036, 0.2773, e_PlayerRole_RB)
    builder.AddPlayer(0.2907, 0.2693, e_PlayerRole_RM)
    builder.AddPlayer(0.3013, -0.0213, e_PlayerRole_DM)
    builder.AddPlayer(0.5307, -0.22, e_PlayerRole_LM)
    builder.AddPlayer(0.5373, 0.0467, e_PlayerRole_DM)
    builder.AddPlayer(0.548, 0.2533, e_PlayerRole_AM)
    builder.AddPlayer(0.7267, 0.2147, e_PlayerRole_AM)
    builder.AddPlayer(0.784, 0.0693, e_PlayerRole_CF)
