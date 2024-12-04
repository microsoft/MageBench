
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
    builder.SetBallPosition(-0.7293, -0.244)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9867, 0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.872, -0.156, e_PlayerRole_LB)
    builder.AddPlayer(-0.82, 0.2747, e_PlayerRole_RB)
    builder.AddPlayer(-0.776, -0.052, e_PlayerRole_CB)
    builder.AddPlayer(-0.7413, -0.2347, e_PlayerRole_LM)
    builder.AddPlayer(-0.7267, 0.0907, e_PlayerRole_DM)
    builder.AddPlayer(-0.6227, -0.1013, e_PlayerRole_LM)
    builder.AddPlayer(-0.484, 0.1467, e_PlayerRole_RM)
    builder.AddPlayer(-0.1813, -0.1453, e_PlayerRole_CM)
    builder.AddPlayer(-0.0733, 0.024, e_PlayerRole_CF)
    builder.AddPlayer(0.132, 0.1547, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9827, -0.0107, e_PlayerRole_GK)
    builder.AddPlayer(-0.368, -0.1427, e_PlayerRole_LB)
    builder.AddPlayer(-0.3053, 0.0373, e_PlayerRole_CB)
    builder.AddPlayer(0.1147, -0.1133, e_PlayerRole_LB)
    builder.AddPlayer(0.1253, 0.228, e_PlayerRole_RM)
    builder.AddPlayer(0.3333, 0.0693, e_PlayerRole_DM)
    builder.AddPlayer(0.5133, 0.2, e_PlayerRole_RM)
    builder.AddPlayer(0.6467, 0.1613, e_PlayerRole_DM)
    builder.AddPlayer(0.7373, 0.364, e_PlayerRole_AM)
    builder.AddPlayer(0.7867, 0.0907, e_PlayerRole_CF)
    builder.AddPlayer(0.8653, 0.2053, e_PlayerRole_AM)
