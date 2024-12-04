
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
    builder.SetBallPosition(0.764, 0.3947)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9067, 0.012, e_PlayerRole_GK)
    builder.AddPlayer(0.152, -0.0187, e_PlayerRole_CB)
    builder.AddPlayer(0.3573, 0.388, e_PlayerRole_RB)
    builder.AddPlayer(0.3773, -0.1747, e_PlayerRole_LB)
    builder.AddPlayer(0.4813, 0.088, e_PlayerRole_DM)
    builder.AddPlayer(0.576, -0.0947, e_PlayerRole_LM)
    builder.AddPlayer(0.6653, 0.1027, e_PlayerRole_DM)
    builder.AddPlayer(0.7533, -0.308, e_PlayerRole_LM)
    builder.AddPlayer(0.7587, 0.3987, e_PlayerRole_AM)
    builder.AddPlayer(0.792, -0.0733, e_PlayerRole_CM)
    builder.AddPlayer(0.8173, 0.0787, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.96, -0.024, e_PlayerRole_GK)
    builder.AddPlayer(-0.952, -0.328, e_PlayerRole_LB)
    builder.AddPlayer(-0.8907, 0.036, e_PlayerRole_CB)
    builder.AddPlayer(-0.8453, 0.2613, e_PlayerRole_RB)
    builder.AddPlayer(-0.752, -0.1907, e_PlayerRole_LM)
    builder.AddPlayer(-0.6827, 0.012, e_PlayerRole_DM)
    builder.AddPlayer(-0.5893, 0.34, e_PlayerRole_RM)
    builder.AddPlayer(-0.5867, -0.2693, e_PlayerRole_LM)
    builder.AddPlayer(-0.5, -0.1307, e_PlayerRole_CM)
    builder.AddPlayer(-0.4453, 0.148, e_PlayerRole_AM)
    builder.AddPlayer(-0.18, -0.0187, e_PlayerRole_CF)
