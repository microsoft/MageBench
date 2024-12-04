
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
    builder.SetBallPosition(-0.1507, -0.2067)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.968, -0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.7253, 0.1027, e_PlayerRole_RB)
    builder.AddPlayer(-0.4773, -0.1427, e_PlayerRole_LB)
    builder.AddPlayer(-0.3147, 0.0307, e_PlayerRole_CB)
    builder.AddPlayer(-0.168, -0.196, e_PlayerRole_LM)
    builder.AddPlayer(-0.1067, 0.2787, e_PlayerRole_RM)
    builder.AddPlayer(0.124, -0.372, e_PlayerRole_LM)
    builder.AddPlayer(0.2147, -0.0107, e_PlayerRole_DM)
    builder.AddPlayer(0.432, -0.3453, e_PlayerRole_CM)
    builder.AddPlayer(0.5347, -0.056, e_PlayerRole_CF)
    builder.AddPlayer(0.568, 0.324, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9693, 0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.5707, -0.1507, e_PlayerRole_LB)
    builder.AddPlayer(-0.5413, 0.112, e_PlayerRole_CB)
    builder.AddPlayer(-0.5053, 0.228, e_PlayerRole_RB)
    builder.AddPlayer(-0.492, 0.3413, e_PlayerRole_RM)
    builder.AddPlayer(-0.2987, 0.0613, e_PlayerRole_DM)
    builder.AddPlayer(-0.2787, 0.1707, e_PlayerRole_RM)
    builder.AddPlayer(-0.176, 0.272, e_PlayerRole_RM)
    builder.AddPlayer(-0.016, -0.1893, e_PlayerRole_CM)
    builder.AddPlayer(0.0653, 0.1507, e_PlayerRole_CF)
    builder.AddPlayer(0.1413, -0.0387, e_PlayerRole_CM)
