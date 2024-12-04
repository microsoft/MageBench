
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
    builder.SetBallPosition(-0.9027, 0.204)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.992, 0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.9147, 0.196, e_PlayerRole_RB)
    builder.AddPlayer(-0.912, -0.048, e_PlayerRole_CB)
    builder.AddPlayer(-0.8573, 0.048, e_PlayerRole_CB)
    builder.AddPlayer(-0.7747, 0.0627, e_PlayerRole_RM)
    builder.AddPlayer(-0.632, -0.152, e_PlayerRole_LM)
    builder.AddPlayer(-0.524, -0.0173, e_PlayerRole_DM)
    builder.AddPlayer(-0.3627, -0.24, e_PlayerRole_LM)
    builder.AddPlayer(-0.1627, -0.1067, e_PlayerRole_CM)
    builder.AddPlayer(-0.1067, 0.0653, e_PlayerRole_AM)
    builder.AddPlayer(0.244, -0.096, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9787, -0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.324, 0.196, e_PlayerRole_RB)
    builder.AddPlayer(-0.236, 0.0187, e_PlayerRole_CB)
    builder.AddPlayer(0.1093, -0.1347, e_PlayerRole_LB)
    builder.AddPlayer(0.176, 0.0653, e_PlayerRole_DM)
    builder.AddPlayer(0.5173, -0.0453, e_PlayerRole_LM)
    builder.AddPlayer(0.6267, 0.116, e_PlayerRole_RM)
    builder.AddPlayer(0.708, -0.164, e_PlayerRole_LM)
    builder.AddPlayer(0.784, -0.104, e_PlayerRole_CM)
    builder.AddPlayer(0.8773, -0.088, e_PlayerRole_CM)
    builder.AddPlayer(0.9493, -0.0, e_PlayerRole_CF)
