
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
    builder.SetBallPosition(-0.104, 0.0227)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9573, -0.008, e_PlayerRole_GK)
    builder.AddPlayer(-0.5893, -0.1467, e_PlayerRole_LB)
    builder.AddPlayer(-0.5027, 0.056, e_PlayerRole_CB)
    builder.AddPlayer(-0.344, 0.2307, e_PlayerRole_RB)
    builder.AddPlayer(-0.3293, -0.256, e_PlayerRole_LM)
    builder.AddPlayer(-0.136, -0.116, e_PlayerRole_LM)
    builder.AddPlayer(-0.108, 0.0373, e_PlayerRole_DM)
    builder.AddPlayer(0.112, -0.2893, e_PlayerRole_LM)
    builder.AddPlayer(0.168, -0.0613, e_PlayerRole_CF)
    builder.AddPlayer(0.424, 0.1413, e_PlayerRole_AM)
    builder.AddPlayer(0.5427, -0.2693, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9813, -0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.6933, 0.156, e_PlayerRole_RB)
    builder.AddPlayer(-0.6027, -0.1933, e_PlayerRole_LB)
    builder.AddPlayer(-0.5173, 0.2507, e_PlayerRole_RB)
    builder.AddPlayer(-0.096, 0.176, e_PlayerRole_RM)
    builder.AddPlayer(-0.0773, 0.0307, e_PlayerRole_DM)
    builder.AddPlayer(0.02, 0.0333, e_PlayerRole_DM)
    builder.AddPlayer(0.3013, 0.12, e_PlayerRole_RM)
    builder.AddPlayer(0.3547, -0.148, e_PlayerRole_CM)
    builder.AddPlayer(0.4253, -0.0653, e_PlayerRole_CM)
    builder.AddPlayer(0.508, 0.132, e_PlayerRole_AM)
