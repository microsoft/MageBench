
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
    builder.SetBallPosition(-0.9747, 0.1987)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9707, 0.0573, e_PlayerRole_GK)
    builder.AddPlayer(-0.9853, 0.192, e_PlayerRole_RB)
    builder.AddPlayer(-0.9, 0.104, e_PlayerRole_RB)
    builder.AddPlayer(-0.6893, 0.1213, e_PlayerRole_RB)
    builder.AddPlayer(-0.6867, -0.0853, e_PlayerRole_DM)
    builder.AddPlayer(-0.5293, -0.092, e_PlayerRole_DM)
    builder.AddPlayer(-0.4027, -0.24, e_PlayerRole_LM)
    builder.AddPlayer(-0.3187, -0.1373, e_PlayerRole_LM)
    builder.AddPlayer(-0.1893, 0.02, e_PlayerRole_CF)
    builder.AddPlayer(-0.036, -0.3, e_PlayerRole_CM)
    builder.AddPlayer(0.0827, -0.0933, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9773, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.2013, 0.1133, e_PlayerRole_CB)
    builder.AddPlayer(-0.18, -0.1947, e_PlayerRole_LB)
    builder.AddPlayer(-0.108, 0.332, e_PlayerRole_RB)
    builder.AddPlayer(0.252, 0.236, e_PlayerRole_RM)
    builder.AddPlayer(0.276, -0.1133, e_PlayerRole_LM)
    builder.AddPlayer(0.4853, 0.164, e_PlayerRole_RM)
    builder.AddPlayer(0.5787, -0.048, e_PlayerRole_LM)
    builder.AddPlayer(0.7347, -0.008, e_PlayerRole_CF)
    builder.AddPlayer(0.7413, -0.2347, e_PlayerRole_CM)
    builder.AddPlayer(0.8027, 0.036, e_PlayerRole_CF)
