
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
    builder.SetBallPosition(-0.7173, -0.0107)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9453, -0.0053, e_PlayerRole_GK)
    builder.AddPlayer(-0.7307, -0.0147, e_PlayerRole_CB)
    builder.AddPlayer(-0.6, 0.276, e_PlayerRole_RB)
    builder.AddPlayer(-0.42, -0.2733, e_PlayerRole_LB)
    builder.AddPlayer(-0.284, -0.132, e_PlayerRole_LM)
    builder.AddPlayer(-0.2493, 0.1227, e_PlayerRole_RM)
    builder.AddPlayer(0.1213, -0.3293, e_PlayerRole_LM)
    builder.AddPlayer(0.1493, 0.2787, e_PlayerRole_RM)
    builder.AddPlayer(0.2067, -0.148, e_PlayerRole_CM)
    builder.AddPlayer(0.4107, 0.012, e_PlayerRole_CF)
    builder.AddPlayer(0.436, 0.2693, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9747, -0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.62, -0.0053, e_PlayerRole_CB)
    builder.AddPlayer(-0.6067, 0.1813, e_PlayerRole_RB)
    builder.AddPlayer(-0.572, -0.2307, e_PlayerRole_LB)
    builder.AddPlayer(-0.4, 0.212, e_PlayerRole_RM)
    builder.AddPlayer(-0.3893, -0.1827, e_PlayerRole_LM)
    builder.AddPlayer(-0.22, -0.2453, e_PlayerRole_LM)
    builder.AddPlayer(0.076, -0.0867, e_PlayerRole_LM)
    builder.AddPlayer(0.108, 0.3187, e_PlayerRole_AM)
    builder.AddPlayer(0.2053, 0.1747, e_PlayerRole_AM)
    builder.AddPlayer(0.476, -0.2133, e_PlayerRole_CM)
