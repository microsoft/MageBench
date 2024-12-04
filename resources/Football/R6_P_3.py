
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
    builder.SetBallPosition(0.3373, -0.0973)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9867, 0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.7427, 0.1693, e_PlayerRole_RB)
    builder.AddPlayer(-0.6413, -0.032, e_PlayerRole_CB)
    builder.AddPlayer(-0.556, -0.1787, e_PlayerRole_LB)
    builder.AddPlayer(-0.5493, 0.1507, e_PlayerRole_RM)
    builder.AddPlayer(-0.4973, -0.0973, e_PlayerRole_LM)
    builder.AddPlayer(-0.332, 0.08, e_PlayerRole_RM)
    builder.AddPlayer(-0.2653, -0.208, e_PlayerRole_LM)
    builder.AddPlayer(-0.1413, 0.008, e_PlayerRole_CF)
    builder.AddPlayer(0.0693, 0.1733, e_PlayerRole_AM)
    builder.AddPlayer(0.3293, -0.0987, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.82, 0.056, e_PlayerRole_GK)
    builder.AddPlayer(-0.532, 0.1013, e_PlayerRole_CB)
    builder.AddPlayer(-0.0987, -0.1493, e_PlayerRole_LB)
    builder.AddPlayer(0.1053, 0.012, e_PlayerRole_CB)
    builder.AddPlayer(0.216, 0.244, e_PlayerRole_RM)
    builder.AddPlayer(0.2933, -0.04, e_PlayerRole_LM)
    builder.AddPlayer(0.4573, 0.1253, e_PlayerRole_RM)
    builder.AddPlayer(0.4747, -0.1307, e_PlayerRole_LM)
    builder.AddPlayer(0.5507, 0.2533, e_PlayerRole_AM)
    builder.AddPlayer(0.564, 0.0187, e_PlayerRole_CF)
    builder.AddPlayer(0.7173, -0.0827, e_PlayerRole_CM)
