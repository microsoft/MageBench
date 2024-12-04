
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
    builder.SetBallPosition(-0.836, -0.0947)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9893, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.9187, 0.0867, e_PlayerRole_CB)
    builder.AddPlayer(-0.8507, 0.3213, e_PlayerRole_RB)
    builder.AddPlayer(-0.8493, -0.096, e_PlayerRole_CB)
    builder.AddPlayer(-0.8333, 0.1067, e_PlayerRole_DM)
    builder.AddPlayer(-0.7653, 0.2147, e_PlayerRole_RM)
    builder.AddPlayer(-0.764, -0.2973, e_PlayerRole_LM)
    builder.AddPlayer(-0.7187, 0.104, e_PlayerRole_DM)
    builder.AddPlayer(-0.688, 0.2987, e_PlayerRole_AM)
    builder.AddPlayer(-0.6213, -0.3453, e_PlayerRole_CM)
    builder.AddPlayer(-0.356, 0.3333, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9893, 0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.2173, 0.0827, e_PlayerRole_CB)
    builder.AddPlayer(0.072, 0.1853, e_PlayerRole_RB)
    builder.AddPlayer(0.3253, -0.0427, e_PlayerRole_LB)
    builder.AddPlayer(0.3267, 0.1347, e_PlayerRole_DM)
    builder.AddPlayer(0.3973, 0.212, e_PlayerRole_RM)
    builder.AddPlayer(0.648, 0.2947, e_PlayerRole_RM)
    builder.AddPlayer(0.7427, 0.0587, e_PlayerRole_DM)
    builder.AddPlayer(0.7493, -0.0427, e_PlayerRole_CM)
    builder.AddPlayer(0.784, 0.248, e_PlayerRole_AM)
    builder.AddPlayer(0.8413, -0.0667, e_PlayerRole_CM)
