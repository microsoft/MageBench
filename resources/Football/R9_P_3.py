
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
    builder.SetBallPosition(0.7453, 0.3253)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9893, 0.0, e_PlayerRole_GK)
    builder.AddPlayer(0.1373, -0.14, e_PlayerRole_CB)
    builder.AddPlayer(0.3893, 0.1493, e_PlayerRole_RB)
    builder.AddPlayer(0.4373, -0.3893, e_PlayerRole_LB)
    builder.AddPlayer(0.4693, -0.0387, e_PlayerRole_DM)
    builder.AddPlayer(0.5107, 0.2013, e_PlayerRole_RM)
    builder.AddPlayer(0.532, -0.38, e_PlayerRole_LM)
    builder.AddPlayer(0.5747, -0.192, e_PlayerRole_LM)
    builder.AddPlayer(0.6493, -0.1187, e_PlayerRole_CF)
    builder.AddPlayer(0.732, 0.3307, e_PlayerRole_AM)
    builder.AddPlayer(0.736, -0.2453, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9813, 0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.8427, -0.0347, e_PlayerRole_CB)
    builder.AddPlayer(-0.8387, -0.2267, e_PlayerRole_LB)
    builder.AddPlayer(-0.8347, 0.2333, e_PlayerRole_RB)
    builder.AddPlayer(-0.7627, 0.1547, e_PlayerRole_DM)
    builder.AddPlayer(-0.6787, 0.0693, e_PlayerRole_DM)
    builder.AddPlayer(-0.6227, -0.2467, e_PlayerRole_LM)
    builder.AddPlayer(-0.58, -0.0053, e_PlayerRole_DM)
    builder.AddPlayer(-0.572, 0.192, e_PlayerRole_AM)
    builder.AddPlayer(-0.4907, -0.1307, e_PlayerRole_CM)
    builder.AddPlayer(-0.4627, 0.3787, e_PlayerRole_AM)
