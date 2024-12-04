
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
    builder.SetBallPosition(0.608, 0.38)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9493, 0.0053, e_PlayerRole_GK)
    builder.AddPlayer(-0.428, -0.168, e_PlayerRole_LB)
    builder.AddPlayer(-0.408, 0.076, e_PlayerRole_CB)
    builder.AddPlayer(-0.1227, -0.184, e_PlayerRole_LB)
    builder.AddPlayer(-0.1067, 0.168, e_PlayerRole_DM)
    builder.AddPlayer(0.3773, 0.3533, e_PlayerRole_RM)
    builder.AddPlayer(0.38, 0.1013, e_PlayerRole_DM)
    builder.AddPlayer(0.4147, -0.1907, e_PlayerRole_LM)
    builder.AddPlayer(0.5707, -0.056, e_PlayerRole_CM)
    builder.AddPlayer(0.576, 0.196, e_PlayerRole_AM)
    builder.AddPlayer(0.6147, 0.38, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9627, -0.0107, e_PlayerRole_GK)
    builder.AddPlayer(-0.7307, -0.1453, e_PlayerRole_CB)
    builder.AddPlayer(-0.7, 0.0173, e_PlayerRole_RB)
    builder.AddPlayer(-0.6613, -0.3413, e_PlayerRole_LB)
    builder.AddPlayer(-0.6027, -0.252, e_PlayerRole_LM)
    builder.AddPlayer(-0.5467, 0.084, e_PlayerRole_RM)
    builder.AddPlayer(-0.5027, -0.1507, e_PlayerRole_DM)
    builder.AddPlayer(-0.4547, -0.276, e_PlayerRole_LM)
    builder.AddPlayer(-0.1293, 0.196, e_PlayerRole_AM)
    builder.AddPlayer(0.0467, -0.0293, e_PlayerRole_CF)
    builder.AddPlayer(0.2587, 0.0413, e_PlayerRole_AM)
