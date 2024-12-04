
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
    builder.SetBallPosition(0.644, -0.012)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9827, 0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.1973, 0.1413, e_PlayerRole_RB)
    builder.AddPlayer(0.088, -0.0973, e_PlayerRole_LB)
    builder.AddPlayer(0.1173, 0.3, e_PlayerRole_RB)
    builder.AddPlayer(0.1293, -0.2733, e_PlayerRole_LM)
    builder.AddPlayer(0.4693, 0.14, e_PlayerRole_RM)
    builder.AddPlayer(0.632, 0.136, e_PlayerRole_RM)
    builder.AddPlayer(0.6347, -0.0147, e_PlayerRole_DM)
    builder.AddPlayer(0.7293, -0.1933, e_PlayerRole_CM)
    builder.AddPlayer(0.8373, 0.16, e_PlayerRole_AM)
    builder.AddPlayer(0.8613, 0.0427, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.984, -0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.8853, -0.1, e_PlayerRole_LB)
    builder.AddPlayer(-0.8547, -0.0, e_PlayerRole_CB)
    builder.AddPlayer(-0.8387, 0.148, e_PlayerRole_RB)
    builder.AddPlayer(-0.7947, -0.1813, e_PlayerRole_LM)
    builder.AddPlayer(-0.7747, -0.052, e_PlayerRole_DM)
    builder.AddPlayer(-0.7333, 0.0347, e_PlayerRole_DM)
    builder.AddPlayer(-0.6747, 0.088, e_PlayerRole_RM)
    builder.AddPlayer(-0.3333, 0.2613, e_PlayerRole_AM)
    builder.AddPlayer(-0.2093, -0.2627, e_PlayerRole_CM)
    builder.AddPlayer(-0.1733, 0.1267, e_PlayerRole_AM)
