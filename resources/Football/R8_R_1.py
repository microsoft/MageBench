
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
    builder.SetBallPosition(-0.3, 0.3773)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9733, 0.0067, e_PlayerRole_GK)
    builder.AddPlayer(-0.7187, -0.244, e_PlayerRole_LB)
    builder.AddPlayer(-0.5093, 0.1547, e_PlayerRole_CB)
    builder.AddPlayer(-0.4707, -0.056, e_PlayerRole_LB)
    builder.AddPlayer(-0.308, 0.3827, e_PlayerRole_RM)
    builder.AddPlayer(-0.2253, 0.276, e_PlayerRole_RM)
    builder.AddPlayer(-0.092, 0.0467, e_PlayerRole_DM)
    builder.AddPlayer(0.084, 0.364, e_PlayerRole_RM)
    builder.AddPlayer(0.1333, -0.1453, e_PlayerRole_CM)
    builder.AddPlayer(0.1587, 0.1533, e_PlayerRole_CF)
    builder.AddPlayer(0.6507, 0.2027, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.952, -0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.6093, -0.1867, e_PlayerRole_CB)
    builder.AddPlayer(-0.52, 0.108, e_PlayerRole_RB)
    builder.AddPlayer(-0.18, -0.2413, e_PlayerRole_LB)
    builder.AddPlayer(-0.0107, -0.336, e_PlayerRole_LM)
    builder.AddPlayer(0.1493, 0.12, e_PlayerRole_RM)
    builder.AddPlayer(0.2133, -0.3547, e_PlayerRole_LM)
    builder.AddPlayer(0.2333, -0.064, e_PlayerRole_DM)
    builder.AddPlayer(0.3747, 0.0933, e_PlayerRole_AM)
    builder.AddPlayer(0.5213, -0.0067, e_PlayerRole_AM)
    builder.AddPlayer(0.6227, -0.2267, e_PlayerRole_CM)
