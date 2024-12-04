
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
    builder.SetBallPosition(0.9387, -0.332)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9373, 0.0013, e_PlayerRole_GK)
    builder.AddPlayer(0.5227, 0.032, e_PlayerRole_RB)
    builder.AddPlayer(0.6627, 0.212, e_PlayerRole_RB)
    builder.AddPlayer(0.7067, -0.2907, e_PlayerRole_LB)
    builder.AddPlayer(0.792, 0.0387, e_PlayerRole_RM)
    builder.AddPlayer(0.8507, -0.0027, e_PlayerRole_DM)
    builder.AddPlayer(0.8693, 0.156, e_PlayerRole_RM)
    builder.AddPlayer(0.8907, 0.0707, e_PlayerRole_RM)
    builder.AddPlayer(0.9053, 0.0627, e_PlayerRole_AM)
    builder.AddPlayer(0.9333, -0.0507, e_PlayerRole_CF)
    builder.AddPlayer(0.96, -0.352, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9773, 0.0347, e_PlayerRole_GK)
    builder.AddPlayer(-0.9813, 0.192, e_PlayerRole_RB)
    builder.AddPlayer(-0.9427, -0.072, e_PlayerRole_LB)
    builder.AddPlayer(-0.9413, 0.0373, e_PlayerRole_CB)
    builder.AddPlayer(-0.94, 0.0627, e_PlayerRole_DM)
    builder.AddPlayer(-0.9213, -0.0533, e_PlayerRole_LM)
    builder.AddPlayer(-0.908, -0.1213, e_PlayerRole_LM)
    builder.AddPlayer(-0.8933, 0.1613, e_PlayerRole_RM)
    builder.AddPlayer(-0.868, -0.0027, e_PlayerRole_CF)
    builder.AddPlayer(-0.84, -0.0267, e_PlayerRole_CM)
    builder.AddPlayer(-0.772, 0.0307, e_PlayerRole_CF)
