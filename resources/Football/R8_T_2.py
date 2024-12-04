
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
    builder.SetBallPosition(0.1187, 0.3413)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.964, 0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.4747, -0.2227, e_PlayerRole_LB)
    builder.AddPlayer(-0.408, -0.0067, e_PlayerRole_CB)
    builder.AddPlayer(-0.2733, -0.268, e_PlayerRole_LB)
    builder.AddPlayer(-0.148, 0.2547, e_PlayerRole_RM)
    builder.AddPlayer(-0.1067, -0.0413, e_PlayerRole_DM)
    builder.AddPlayer(0.0787, -0.2653, e_PlayerRole_LM)
    builder.AddPlayer(0.1267, 0.3533, e_PlayerRole_RM)
    builder.AddPlayer(0.1613, -0.04, e_PlayerRole_CF)
    builder.AddPlayer(0.3853, 0.04, e_PlayerRole_CF)
    builder.AddPlayer(0.5773, -0.112, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9733, 0.016, e_PlayerRole_GK)
    builder.AddPlayer(-0.6613, 0.1853, e_PlayerRole_RB)
    builder.AddPlayer(-0.472, -0.2013, e_PlayerRole_LB)
    builder.AddPlayer(-0.356, 0.2733, e_PlayerRole_RB)
    builder.AddPlayer(-0.2627, -0.3573, e_PlayerRole_LM)
    builder.AddPlayer(-0.2533, -0.2293, e_PlayerRole_LM)
    builder.AddPlayer(-0.1413, -0.2187, e_PlayerRole_LM)
    builder.AddPlayer(-0.1053, 0.2053, e_PlayerRole_RM)
    builder.AddPlayer(0.076, 0.008, e_PlayerRole_CF)
    builder.AddPlayer(0.2227, 0.2893, e_PlayerRole_AM)
    builder.AddPlayer(0.44, 0.028, e_PlayerRole_CF)
