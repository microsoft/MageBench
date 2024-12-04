
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
    builder.SetBallPosition(0.8227, 0.0173)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9547, 0.004, e_PlayerRole_GK)
    builder.AddPlayer(0.4827, 0.1453, e_PlayerRole_RB)
    builder.AddPlayer(0.5747, -0.0787, e_PlayerRole_CB)
    builder.AddPlayer(0.656, -0.284, e_PlayerRole_LB)
    builder.AddPlayer(0.8107, 0.0187, e_PlayerRole_RM)
    builder.AddPlayer(0.828, 0.1893, e_PlayerRole_RM)
    builder.AddPlayer(0.856, -0.18, e_PlayerRole_LM)
    builder.AddPlayer(0.884, 0.016, e_PlayerRole_RM)
    builder.AddPlayer(0.8893, -0.0987, e_PlayerRole_CF)
    builder.AddPlayer(0.948, 0.1653, e_PlayerRole_AM)
    builder.AddPlayer(0.9493, -0.3453, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.976, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.9667, 0.0547, e_PlayerRole_CB)
    builder.AddPlayer(-0.932, 0.064, e_PlayerRole_CB)
    builder.AddPlayer(-0.9107, -0.124, e_PlayerRole_LB)
    builder.AddPlayer(-0.9053, -0.0453, e_PlayerRole_LM)
    builder.AddPlayer(-0.896, 0.004, e_PlayerRole_DM)
    builder.AddPlayer(-0.8653, 0.164, e_PlayerRole_RM)
    builder.AddPlayer(-0.8547, -0.064, e_PlayerRole_LM)
    builder.AddPlayer(-0.8453, 0.0107, e_PlayerRole_CF)
    builder.AddPlayer(-0.7787, 0.256, e_PlayerRole_AM)
    builder.AddPlayer(-0.708, 0.1547, e_PlayerRole_AM)
