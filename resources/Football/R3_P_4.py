
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
    builder.SetBallPosition(0.5493, -0.3987)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9787, 0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.5053, 0.1773, e_PlayerRole_RB)
    builder.AddPlayer(-0.2547, -0.0853, e_PlayerRole_CB)
    builder.AddPlayer(0.1293, -0.0973, e_PlayerRole_CB)
    builder.AddPlayer(0.2493, -0.348, e_PlayerRole_LM)
    builder.AddPlayer(0.356, -0.2133, e_PlayerRole_LM)
    builder.AddPlayer(0.38, -0.0387, e_PlayerRole_DM)
    builder.AddPlayer(0.444, -0.2253, e_PlayerRole_LM)
    builder.AddPlayer(0.5293, -0.272, e_PlayerRole_CM)
    builder.AddPlayer(0.54, -0.0333, e_PlayerRole_CF)
    builder.AddPlayer(0.5413, -0.4, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9827, -0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.7, 0.256, e_PlayerRole_RB)
    builder.AddPlayer(-0.608, 0.2933, e_PlayerRole_RB)
    builder.AddPlayer(-0.6013, 0.2293, e_PlayerRole_CB)
    builder.AddPlayer(-0.5947, -0.036, e_PlayerRole_LM)
    builder.AddPlayer(-0.5427, 0.3373, e_PlayerRole_RM)
    builder.AddPlayer(-0.432, 0.3093, e_PlayerRole_RM)
    builder.AddPlayer(-0.4173, 0.1013, e_PlayerRole_LM)
    builder.AddPlayer(-0.3347, 0.32, e_PlayerRole_AM)
    builder.AddPlayer(-0.28, 0.3853, e_PlayerRole_AM)
    builder.AddPlayer(-0.1747, 0.1787, e_PlayerRole_CF)
