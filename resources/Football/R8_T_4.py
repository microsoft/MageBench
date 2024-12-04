
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
    builder.SetBallPosition(-0.1227, 0.3413)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9733, 0.0067, e_PlayerRole_GK)
    builder.AddPlayer(-0.608, 0.268, e_PlayerRole_RB)
    builder.AddPlayer(-0.3947, 0.0067, e_PlayerRole_CB)
    builder.AddPlayer(-0.3853, 0.176, e_PlayerRole_CB)
    builder.AddPlayer(-0.3533, -0.1413, e_PlayerRole_LM)
    builder.AddPlayer(-0.1307, 0.352, e_PlayerRole_RM)
    builder.AddPlayer(-0.0547, 0.2107, e_PlayerRole_RM)
    builder.AddPlayer(-0.0373, -0.188, e_PlayerRole_LM)
    builder.AddPlayer(0.112, -0.1107, e_PlayerRole_CM)
    builder.AddPlayer(0.26, 0.068, e_PlayerRole_CF)
    builder.AddPlayer(0.2667, 0.396, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9413, 0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.5173, 0.2773, e_PlayerRole_RB)
    builder.AddPlayer(-0.3267, -0.0787, e_PlayerRole_CB)
    builder.AddPlayer(-0.168, 0.096, e_PlayerRole_RB)
    builder.AddPlayer(0.012, -0.2787, e_PlayerRole_LM)
    builder.AddPlayer(0.0333, -0.3787, e_PlayerRole_LM)
    builder.AddPlayer(0.0667, 0.2253, e_PlayerRole_RM)
    builder.AddPlayer(0.2413, 0.1067, e_PlayerRole_RM)
    builder.AddPlayer(0.3227, -0.216, e_PlayerRole_CM)
    builder.AddPlayer(0.5027, -0.0013, e_PlayerRole_CF)
    builder.AddPlayer(0.5987, -0.3493, e_PlayerRole_CM)
