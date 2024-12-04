
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
    builder.SetBallPosition(-0.0893, -0.0653)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9787, 0.0, e_PlayerRole_GK)
    builder.AddPlayer(-0.5187, -0.1027, e_PlayerRole_LB)
    builder.AddPlayer(-0.484, 0.128, e_PlayerRole_RB)
    builder.AddPlayer(-0.2347, -0.236, e_PlayerRole_LB)
    builder.AddPlayer(-0.18, 0.0507, e_PlayerRole_DM)
    builder.AddPlayer(-0.1493, 0.2787, e_PlayerRole_RM)
    builder.AddPlayer(-0.1013, -0.072, e_PlayerRole_LM)
    builder.AddPlayer(0.084, 0.0653, e_PlayerRole_DM)
    builder.AddPlayer(0.1333, 0.2467, e_PlayerRole_AM)
    builder.AddPlayer(0.34, -0.2307, e_PlayerRole_CM)
    builder.AddPlayer(0.5307, 0.0427, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9693, 0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.6453, -0.1947, e_PlayerRole_LB)
    builder.AddPlayer(-0.6013, 0.0693, e_PlayerRole_RB)
    builder.AddPlayer(-0.292, 0.2, e_PlayerRole_RB)
    builder.AddPlayer(-0.1907, -0.3053, e_PlayerRole_LM)
    builder.AddPlayer(0.02, 0.1213, e_PlayerRole_RM)
    builder.AddPlayer(0.1533, -0.0333, e_PlayerRole_DM)
    builder.AddPlayer(0.2467, -0.2947, e_PlayerRole_LM)
    builder.AddPlayer(0.256, 0.24, e_PlayerRole_AM)
    builder.AddPlayer(0.4093, -0.144, e_PlayerRole_CM)
    builder.AddPlayer(0.5867, 0.1227, e_PlayerRole_AM)
