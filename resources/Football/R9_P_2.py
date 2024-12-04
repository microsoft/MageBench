
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
    builder.SetBallPosition(0.6867, 0.1347)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9907, 0.0013, e_PlayerRole_GK)
    builder.AddPlayer(0.1027, -0.244, e_PlayerRole_LB)
    builder.AddPlayer(0.1253, 0.0187, e_PlayerRole_CB)
    builder.AddPlayer(0.2507, -0.14, e_PlayerRole_CB)
    builder.AddPlayer(0.408, 0.2773, e_PlayerRole_RM)
    builder.AddPlayer(0.5293, -0.14, e_PlayerRole_DM)
    builder.AddPlayer(0.5347, -0.3787, e_PlayerRole_LM)
    builder.AddPlayer(0.6253, 0.012, e_PlayerRole_DM)
    builder.AddPlayer(0.6533, -0.264, e_PlayerRole_CM)
    builder.AddPlayer(0.6787, 0.1413, e_PlayerRole_AM)
    builder.AddPlayer(0.8293, -0.3227, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.936, -0.0333, e_PlayerRole_GK)
    builder.AddPlayer(-0.8187, -0.0067, e_PlayerRole_CB)
    builder.AddPlayer(-0.8173, 0.2947, e_PlayerRole_RB)
    builder.AddPlayer(-0.7027, 0.092, e_PlayerRole_CB)
    builder.AddPlayer(-0.668, 0.2173, e_PlayerRole_RM)
    builder.AddPlayer(-0.6533, -0.052, e_PlayerRole_DM)
    builder.AddPlayer(-0.5507, 0.1027, e_PlayerRole_DM)
    builder.AddPlayer(-0.548, 0.2973, e_PlayerRole_RM)
    builder.AddPlayer(-0.504, -0.1307, e_PlayerRole_CM)
    builder.AddPlayer(-0.4347, -0.2693, e_PlayerRole_CM)
    builder.AddPlayer(-0.3307, 0.1173, e_PlayerRole_AM)
