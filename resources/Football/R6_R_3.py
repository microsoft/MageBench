
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
    builder.SetBallPosition(0.7227, 0.0053)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9667, -0.008, e_PlayerRole_GK)
    builder.AddPlayer(0.212, -0.1853, e_PlayerRole_LB)
    builder.AddPlayer(0.2253, 0.2053, e_PlayerRole_RB)
    builder.AddPlayer(0.328, -0.0533, e_PlayerRole_CB)
    builder.AddPlayer(0.3667, 0.124, e_PlayerRole_RM)
    builder.AddPlayer(0.4147, -0.224, e_PlayerRole_LM)
    builder.AddPlayer(0.6453, -0.0707, e_PlayerRole_DM)
    builder.AddPlayer(0.6893, -0.2427, e_PlayerRole_LM)
    builder.AddPlayer(0.7093, 0.18, e_PlayerRole_AM)
    builder.AddPlayer(0.7333, 0.0133, e_PlayerRole_CF)
    builder.AddPlayer(0.836, 0.0107, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.976, -0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.86, -0.04, e_PlayerRole_LB)
    builder.AddPlayer(-0.8187, 0.048, e_PlayerRole_CB)
    builder.AddPlayer(-0.776, -0.0373, e_PlayerRole_LB)
    builder.AddPlayer(-0.7427, -0.0827, e_PlayerRole_LM)
    builder.AddPlayer(-0.7413, 0.16, e_PlayerRole_RM)
    builder.AddPlayer(-0.6973, 0.056, e_PlayerRole_DM)
    builder.AddPlayer(-0.584, 0.0573, e_PlayerRole_DM)
    builder.AddPlayer(-0.512, -0.016, e_PlayerRole_CM)
    builder.AddPlayer(-0.3547, -0.0813, e_PlayerRole_CM)
    builder.AddPlayer(-0.2547, 0.164, e_PlayerRole_AM)
