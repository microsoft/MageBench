
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
    builder.SetBallPosition(-0.1773, 0.084)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9693, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.7453, 0.0947, e_PlayerRole_RB)
    builder.AddPlayer(-0.6533, -0.2747, e_PlayerRole_LB)
    builder.AddPlayer(-0.3507, 0.2467, e_PlayerRole_RB)
    builder.AddPlayer(-0.3133, -0.0707, e_PlayerRole_DM)
    builder.AddPlayer(-0.1893, 0.0853, e_PlayerRole_RM)
    builder.AddPlayer(0.06, -0.3893, e_PlayerRole_LM)
    builder.AddPlayer(0.1173, -0.0307, e_PlayerRole_DM)
    builder.AddPlayer(0.4107, -0.1787, e_PlayerRole_CM)
    builder.AddPlayer(0.4773, 0.2987, e_PlayerRole_AM)
    builder.AddPlayer(0.66, 0.0147, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9747, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.808, 0.1013, e_PlayerRole_RB)
    builder.AddPlayer(-0.7027, 0.2227, e_PlayerRole_RB)
    builder.AddPlayer(-0.604, -0.0053, e_PlayerRole_CB)
    builder.AddPlayer(-0.5747, -0.3053, e_PlayerRole_LM)
    builder.AddPlayer(-0.5587, -0.1093, e_PlayerRole_LM)
    builder.AddPlayer(-0.4533, 0.1267, e_PlayerRole_RM)
    builder.AddPlayer(-0.2027, -0.1133, e_PlayerRole_LM)
    builder.AddPlayer(-0.14, 0.292, e_PlayerRole_AM)
    builder.AddPlayer(0.052, -0.012, e_PlayerRole_CF)
    builder.AddPlayer(0.4947, 0.176, e_PlayerRole_AM)
