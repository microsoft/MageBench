
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
    builder.SetBallPosition(-0.132, -0.068)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.972, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.556, 0.0653, e_PlayerRole_RB)
    builder.AddPlayer(-0.4787, -0.208, e_PlayerRole_LM)
    builder.AddPlayer(-0.2547, 0.0547, e_PlayerRole_RM)
    builder.AddPlayer(-0.1467, -0.0693, e_PlayerRole_CF)
    builder.AddPlayer(0.3067, 0.064, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.972, 0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.5467, 0.092, e_PlayerRole_CB)
    builder.AddPlayer(-0.2933, -0.0587, e_PlayerRole_LB)
    builder.AddPlayer(-0.2573, 0.1747, e_PlayerRole_RM)
    builder.AddPlayer(-0.036, 0.0933, e_PlayerRole_DM)
    builder.AddPlayer(0.2373, -0.0547, e_PlayerRole_LM)
    builder.AddPlayer(0.2467, -0.0413, e_PlayerRole_CM)
    builder.AddPlayer(0.464, 0.2, e_PlayerRole_AM)
    builder.AddPlayer(0.5427, -0.0587, e_PlayerRole_CM)
