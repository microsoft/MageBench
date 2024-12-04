
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
    builder.SetBallPosition(-0.7653, -0.148)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.7773, -0.1467, e_PlayerRole_GK)
    builder.AddPlayer(-0.6973, -0.1147, e_PlayerRole_CB)
    builder.AddPlayer(-0.6747, 0.168, e_PlayerRole_RB)
    builder.AddPlayer(-0.4187, -0.2667, e_PlayerRole_LB)
    builder.AddPlayer(-0.184, -0.008, e_PlayerRole_DM)
    builder.AddPlayer(-0.076, 0.2373, e_PlayerRole_RM)
    builder.AddPlayer(0.0747, -0.0827, e_PlayerRole_DM)
    builder.AddPlayer(0.1133, -0.28, e_PlayerRole_LM)
    builder.AddPlayer(0.1347, 0.216, e_PlayerRole_AM)
    builder.AddPlayer(0.2413, 0.0173, e_PlayerRole_CF)
    builder.AddPlayer(0.248, -0.1867, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9733, 0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.436, 0.324, e_PlayerRole_RB)
    builder.AddPlayer(-0.3587, -0.184, e_PlayerRole_LB)
    builder.AddPlayer(-0.3547, 0.0507, e_PlayerRole_CB)
    builder.AddPlayer(-0.2333, 0.36, e_PlayerRole_RM)
    builder.AddPlayer(-0.1907, 0.176, e_PlayerRole_DM)
    builder.AddPlayer(-0.1147, -0.1, e_PlayerRole_LM)
    builder.AddPlayer(0.0653, -0.14, e_PlayerRole_LM)
    builder.AddPlayer(0.2627, 0.3347, e_PlayerRole_AM)
    builder.AddPlayer(0.428, -0.0387, e_PlayerRole_CM)
    builder.AddPlayer(0.5347, 0.1307, e_PlayerRole_CF)
