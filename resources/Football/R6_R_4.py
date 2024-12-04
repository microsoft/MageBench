
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
    builder.SetBallPosition(0.588, 0.12)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9427, -0.0053, e_PlayerRole_GK)
    builder.AddPlayer(0.1973, -0.224, e_PlayerRole_LB)
    builder.AddPlayer(0.2387, 0.036, e_PlayerRole_RB)
    builder.AddPlayer(0.456, -0.16, e_PlayerRole_LB)
    builder.AddPlayer(0.528, -0.0133, e_PlayerRole_DM)
    builder.AddPlayer(0.548, 0.0907, e_PlayerRole_RM)
    builder.AddPlayer(0.5667, 0.1613, e_PlayerRole_RM)
    builder.AddPlayer(0.7027, -0.228, e_PlayerRole_LM)
    builder.AddPlayer(0.7653, -0.096, e_PlayerRole_CF)
    builder.AddPlayer(0.772, -0.1853, e_PlayerRole_CM)
    builder.AddPlayer(0.78, 0.064, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.976, 0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.8067, -0.1747, e_PlayerRole_LB)
    builder.AddPlayer(-0.796, -0.1467, e_PlayerRole_LB)
    builder.AddPlayer(-0.7947, -0.1107, e_PlayerRole_LB)
    builder.AddPlayer(-0.792, -0.016, e_PlayerRole_LM)
    builder.AddPlayer(-0.7813, 0.0667, e_PlayerRole_DM)
    builder.AddPlayer(-0.76, 0.1547, e_PlayerRole_DM)
    builder.AddPlayer(-0.7387, 0.2093, e_PlayerRole_RM)
    builder.AddPlayer(-0.724, 0.0213, e_PlayerRole_CF)
    builder.AddPlayer(-0.7107, 0.124, e_PlayerRole_CF)
    builder.AddPlayer(-0.3827, 0.3627, e_PlayerRole_AM)
