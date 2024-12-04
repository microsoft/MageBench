
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
    builder.SetBallPosition(-0.6933, -0.3293)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9867, 0.008, e_PlayerRole_GK)
    builder.AddPlayer(-0.868, -0.0373, e_PlayerRole_RB)
    builder.AddPlayer(-0.7773, -0.0133, e_PlayerRole_RB)
    builder.AddPlayer(-0.7133, -0.332, e_PlayerRole_LM)
    builder.AddPlayer(-0.6267, 0.0093, e_PlayerRole_RM)
    builder.AddPlayer(-0.4893, -0.0067, e_PlayerRole_AM)
    builder.AddPlayer(-0.4067, -0.0453, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9787, 0.012, e_PlayerRole_GK)
    builder.AddPlayer(0.472, 0.1547, e_PlayerRole_CB)
    builder.AddPlayer(0.5493, 0.1333, e_PlayerRole_CB)
    builder.AddPlayer(0.5747, 0.3293, e_PlayerRole_RM)
    builder.AddPlayer(0.6453, 0.272, e_PlayerRole_RM)
    builder.AddPlayer(0.6813, 0.104, e_PlayerRole_LM)
    builder.AddPlayer(0.7813, 0.0973, e_PlayerRole_CM)
    builder.AddPlayer(0.8707, 0.1013, e_PlayerRole_CM)
