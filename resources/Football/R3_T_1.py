
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
    builder.SetBallPosition(0.9827, -0.404)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.988, 0.004, e_PlayerRole_GK)
    builder.AddPlayer(0.44, -0.008, e_PlayerRole_CB)
    builder.AddPlayer(0.512, -0.176, e_PlayerRole_CB)
    builder.AddPlayer(0.5827, 0.2027, e_PlayerRole_RB)
    builder.AddPlayer(0.72, -0.0333, e_PlayerRole_DM)
    builder.AddPlayer(0.7533, -0.2987, e_PlayerRole_LM)
    builder.AddPlayer(0.7787, 0.0573, e_PlayerRole_RM)
    builder.AddPlayer(0.8173, -0.1493, e_PlayerRole_DM)
    builder.AddPlayer(0.888, 0.168, e_PlayerRole_AM)
    builder.AddPlayer(0.8987, -0.0373, e_PlayerRole_CF)
    builder.AddPlayer(0.9947, -0.4107, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9853, -0.0067, e_PlayerRole_GK)
    builder.AddPlayer(-0.9133, 0.1693, e_PlayerRole_RB)
    builder.AddPlayer(-0.884, -0.0773, e_PlayerRole_CB)
    builder.AddPlayer(-0.8507, -0.24, e_PlayerRole_LB)
    builder.AddPlayer(-0.816, 0.0347, e_PlayerRole_RM)
    builder.AddPlayer(-0.7387, -0.1493, e_PlayerRole_DM)
    builder.AddPlayer(-0.6907, 0.1667, e_PlayerRole_RM)
    builder.AddPlayer(-0.6893, -0.36, e_PlayerRole_LM)
    builder.AddPlayer(-0.648, -0.0413, e_PlayerRole_CF)
    builder.AddPlayer(-0.6067, 0.08, e_PlayerRole_AM)
    builder.AddPlayer(-0.5293, -0.1627, e_PlayerRole_CF)
