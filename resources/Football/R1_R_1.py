
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
    builder.SetBallPosition(-0.7307, -0.288)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9907, -0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.7787, 0.204, e_PlayerRole_RB)
    builder.AddPlayer(-0.7413, -0.2907, e_PlayerRole_LB)
    builder.AddPlayer(-0.5507, -0.0733, e_PlayerRole_CB)
    builder.AddPlayer(-0.524, -0.1733, e_PlayerRole_DM)
    builder.AddPlayer(-0.416, -0.368, e_PlayerRole_LM)
    builder.AddPlayer(-0.4053, 0.204, e_PlayerRole_RM)
    builder.AddPlayer(-0.28, -0.0293, e_PlayerRole_DM)
    builder.AddPlayer(-0.2133, -0.2973, e_PlayerRole_CM)
    builder.AddPlayer(0.1467, 0.0947, e_PlayerRole_AM)
    builder.AddPlayer(0.172, -0.268, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9773, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.3053, 0.1333, e_PlayerRole_CB)
    builder.AddPlayer(-0.2907, 0.268, e_PlayerRole_RB)
    builder.AddPlayer(-0.2547, -0.1227, e_PlayerRole_LB)
    builder.AddPlayer(-0.2387, -0.0093, e_PlayerRole_LM)
    builder.AddPlayer(0.16, 0.0973, e_PlayerRole_DM)
    builder.AddPlayer(0.2373, -0.0893, e_PlayerRole_LM)
    builder.AddPlayer(0.4013, 0.364, e_PlayerRole_RM)
    builder.AddPlayer(0.44, 0.344, e_PlayerRole_AM)
    builder.AddPlayer(0.604, 0.2653, e_PlayerRole_AM)
    builder.AddPlayer(0.6107, -0.0227, e_PlayerRole_CM)
