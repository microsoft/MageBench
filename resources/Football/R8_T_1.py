
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
    builder.SetBallPosition(-0.1547, 0.3413)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9707, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.64, 0.0453, e_PlayerRole_CB)
    builder.AddPlayer(-0.5013, -0.132, e_PlayerRole_LB)
    builder.AddPlayer(-0.4853, 0.2627, e_PlayerRole_RB)
    builder.AddPlayer(-0.2013, -0.2147, e_PlayerRole_LM)
    builder.AddPlayer(-0.1947, 0.0027, e_PlayerRole_DM)
    builder.AddPlayer(-0.1747, 0.34, e_PlayerRole_RM)
    builder.AddPlayer(0.0213, 0.224, e_PlayerRole_RM)
    builder.AddPlayer(0.2173, 0.324, e_PlayerRole_AM)
    builder.AddPlayer(0.2813, 0.0973, e_PlayerRole_CF)
    builder.AddPlayer(0.3053, -0.196, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9653, 0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.6773, 0.212, e_PlayerRole_RB)
    builder.AddPlayer(-0.6053, -0.3227, e_PlayerRole_LB)
    builder.AddPlayer(-0.3373, 0.176, e_PlayerRole_RB)
    builder.AddPlayer(-0.2187, -0.1187, e_PlayerRole_DM)
    builder.AddPlayer(-0.0467, -0.3147, e_PlayerRole_LM)
    builder.AddPlayer(0.06, 0.2173, e_PlayerRole_RM)
    builder.AddPlayer(0.1133, 0.0827, e_PlayerRole_RM)
    builder.AddPlayer(0.1707, -0.1827, e_PlayerRole_CM)
    builder.AddPlayer(0.3627, 0.2173, e_PlayerRole_AM)
    builder.AddPlayer(0.4133, -0.0253, e_PlayerRole_CF)
