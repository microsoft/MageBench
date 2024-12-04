
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
    builder.SetBallPosition(-0.736, -0.0187)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.7573, -0.024, e_PlayerRole_GK)
    builder.AddPlayer(-0.5853, -0.156, e_PlayerRole_LB)
    builder.AddPlayer(-0.4333, 0.1773, e_PlayerRole_RB)
    builder.AddPlayer(-0.3813, -0.16, e_PlayerRole_LB)
    builder.AddPlayer(-0.3613, 0.024, e_PlayerRole_DM)
    builder.AddPlayer(-0.2387, 0.1867, e_PlayerRole_RM)
    builder.AddPlayer(-0.1987, -0.3467, e_PlayerRole_LM)
    builder.AddPlayer(-0.1147, -0.2027, e_PlayerRole_LM)
    builder.AddPlayer(-0.0773, -0.088, e_PlayerRole_CF)
    builder.AddPlayer(-0.0707, 0.2853, e_PlayerRole_AM)
    builder.AddPlayer(0.0827, 0.0987, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.972, -0.0, e_PlayerRole_GK)
    builder.AddPlayer(-0.352, 0.2387, e_PlayerRole_RB)
    builder.AddPlayer(-0.272, 0.0747, e_PlayerRole_CB)
    builder.AddPlayer(-0.2133, -0.1333, e_PlayerRole_LB)
    builder.AddPlayer(-0.0827, 0.0253, e_PlayerRole_DM)
    builder.AddPlayer(0.02, 0.1973, e_PlayerRole_RM)
    builder.AddPlayer(0.1493, -0.092, e_PlayerRole_LM)
    builder.AddPlayer(0.1493, 0.2587, e_PlayerRole_RM)
    builder.AddPlayer(0.2813, 0.34, e_PlayerRole_AM)
    builder.AddPlayer(0.4493, 0.2147, e_PlayerRole_AM)
    builder.AddPlayer(0.5053, 0.0227, e_PlayerRole_CM)
