
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
    builder.SetBallPosition(0.5373, -0.264)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.984, -0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.3627, 0.1987, e_PlayerRole_RB)
    builder.AddPlayer(-0.0373, -0.0453, e_PlayerRole_CB)
    builder.AddPlayer(0.0347, -0.3, e_PlayerRole_LB)
    builder.AddPlayer(0.1667, 0.1973, e_PlayerRole_RM)
    builder.AddPlayer(0.2613, -0.1547, e_PlayerRole_LM)
    builder.AddPlayer(0.4987, -0.1893, e_PlayerRole_LM)
    builder.AddPlayer(0.5347, -0.272, e_PlayerRole_LM)
    builder.AddPlayer(0.5627, 0.1267, e_PlayerRole_AM)
    builder.AddPlayer(0.7373, -0.2893, e_PlayerRole_CM)
    builder.AddPlayer(0.7653, -0.0013, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9707, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.8693, -0.092, e_PlayerRole_LB)
    builder.AddPlayer(-0.86, 0.004, e_PlayerRole_LB)
    builder.AddPlayer(-0.8253, 0.1693, e_PlayerRole_CB)
    builder.AddPlayer(-0.7773, 0.26, e_PlayerRole_RM)
    builder.AddPlayer(-0.72, 0.0333, e_PlayerRole_LM)
    builder.AddPlayer(-0.6413, 0.2387, e_PlayerRole_RM)
    builder.AddPlayer(-0.6267, 0.176, e_PlayerRole_DM)
    builder.AddPlayer(-0.3467, 0.1373, e_PlayerRole_CF)
    builder.AddPlayer(-0.124, 0.3107, e_PlayerRole_AM)
    builder.AddPlayer(-0.0653, 0.0693, e_PlayerRole_CF)
