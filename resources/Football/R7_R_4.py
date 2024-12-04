
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
    builder.SetBallPosition(-0.676, 0.364)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9613, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.6947, 0.376, e_PlayerRole_RB)
    builder.AddPlayer(-0.6747, 0.1013, e_PlayerRole_CB)
    builder.AddPlayer(-0.564, -0.16, e_PlayerRole_LB)
    builder.AddPlayer(-0.5, 0.204, e_PlayerRole_RM)
    builder.AddPlayer(-0.3453, 0.0253, e_PlayerRole_DM)
    builder.AddPlayer(-0.2507, 0.2, e_PlayerRole_RM)
    builder.AddPlayer(-0.1867, -0.0307, e_PlayerRole_DM)
    builder.AddPlayer(-0.048, -0.304, e_PlayerRole_CM)
    builder.AddPlayer(0.0787, 0.1867, e_PlayerRole_AM)
    builder.AddPlayer(0.0907, -0.0427, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9587, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.224, 0.1613, e_PlayerRole_RB)
    builder.AddPlayer(-0.212, -0.0787, e_PlayerRole_CB)
    builder.AddPlayer(-0.196, -0.3147, e_PlayerRole_LB)
    builder.AddPlayer(-0.0587, 0.196, e_PlayerRole_RM)
    builder.AddPlayer(-0.008, -0.1, e_PlayerRole_DM)
    builder.AddPlayer(0.136, -0.256, e_PlayerRole_LM)
    builder.AddPlayer(0.3747, -0.112, e_PlayerRole_DM)
    builder.AddPlayer(0.54, -0.316, e_PlayerRole_CM)
    builder.AddPlayer(0.5507, -0.0307, e_PlayerRole_CF)
    builder.AddPlayer(0.564, -0.16, e_PlayerRole_CM)
