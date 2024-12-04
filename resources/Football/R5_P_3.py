
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
    builder.SetBallPosition(-0.092, -0.0453)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9813, 0.0053, e_PlayerRole_GK)
    builder.AddPlayer(-0.8707, 0.0907, e_PlayerRole_RB)
    builder.AddPlayer(-0.7387, 0.2147, e_PlayerRole_RB)
    builder.AddPlayer(-0.7067, 0.02, e_PlayerRole_DM)
    builder.AddPlayer(-0.6373, -0.2053, e_PlayerRole_LM)
    builder.AddPlayer(-0.3133, 0.0453, e_PlayerRole_CF)
    builder.AddPlayer(-0.1187, -0.0467, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9733, 0.0067, e_PlayerRole_GK)
    builder.AddPlayer(-0.3987, -0.116, e_PlayerRole_LB)
    builder.AddPlayer(-0.1933, 0.1107, e_PlayerRole_RB)
    builder.AddPlayer(0.248, 0.1053, e_PlayerRole_RM)
    builder.AddPlayer(0.2787, -0.0107, e_PlayerRole_DM)
    builder.AddPlayer(0.4893, 0.1813, e_PlayerRole_RM)
    builder.AddPlayer(0.5893, -0.116, e_PlayerRole_CM)
    builder.AddPlayer(0.672, 0.0253, e_PlayerRole_CF)
    builder.AddPlayer(0.684, -0.0187, e_PlayerRole_CM)
