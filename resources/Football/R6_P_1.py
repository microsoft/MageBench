
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
    builder.SetBallPosition(0.7147, 0.052)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9893, 0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.4373, -0.004, e_PlayerRole_CB)
    builder.AddPlayer(-0.1907, 0.216, e_PlayerRole_RB)
    builder.AddPlayer(0.272, -0.104, e_PlayerRole_LB)
    builder.AddPlayer(0.4427, 0.2867, e_PlayerRole_RM)
    builder.AddPlayer(0.476, 0.0507, e_PlayerRole_DM)
    builder.AddPlayer(0.5213, -0.18, e_PlayerRole_LM)
    builder.AddPlayer(0.6733, -0.0693, e_PlayerRole_DM)
    builder.AddPlayer(0.6827, 0.2613, e_PlayerRole_AM)
    builder.AddPlayer(0.6987, 0.0533, e_PlayerRole_CF)
    builder.AddPlayer(0.8573, -0.2773, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.964, 0.0333, e_PlayerRole_GK)
    builder.AddPlayer(-0.8173, -0.264, e_PlayerRole_LB)
    builder.AddPlayer(-0.8173, 0.212, e_PlayerRole_RB)
    builder.AddPlayer(-0.784, 0.004, e_PlayerRole_CB)
    builder.AddPlayer(-0.6893, -0.2267, e_PlayerRole_LM)
    builder.AddPlayer(-0.6773, 0.04, e_PlayerRole_DM)
    builder.AddPlayer(-0.652, 0.2693, e_PlayerRole_RM)
    builder.AddPlayer(-0.5413, 0.164, e_PlayerRole_RM)
    builder.AddPlayer(-0.5133, -0.048, e_PlayerRole_CF)
    builder.AddPlayer(-0.5053, -0.2387, e_PlayerRole_CM)
    builder.AddPlayer(-0.3053, 0.088, e_PlayerRole_CF)
