
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
    builder.SetBallPosition(-0.0653, -0.0627)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9933, -0.0053, e_PlayerRole_GK)
    builder.AddPlayer(-0.5813, 0.0067, e_PlayerRole_CB)
    builder.AddPlayer(-0.4547, -0.108, e_PlayerRole_LB)
    builder.AddPlayer(-0.4533, 0.088, e_PlayerRole_RB)
    builder.AddPlayer(-0.2787, 0.2133, e_PlayerRole_RM)
    builder.AddPlayer(-0.0747, -0.068, e_PlayerRole_LM)
    builder.AddPlayer(0.08, 0.056, e_PlayerRole_DM)
    builder.AddPlayer(0.1707, -0.1333, e_PlayerRole_LM)
    builder.AddPlayer(0.624, 0.024, e_PlayerRole_CF)
    builder.AddPlayer(0.6493, -0.1973, e_PlayerRole_CM)
    builder.AddPlayer(0.796, 0.184, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9867, -0.0, e_PlayerRole_GK)
    builder.AddPlayer(-0.8387, -0.1733, e_PlayerRole_LB)
    builder.AddPlayer(-0.7093, 0.1973, e_PlayerRole_RB)
    builder.AddPlayer(-0.6667, 0.0373, e_PlayerRole_CB)
    builder.AddPlayer(-0.076, 0.052, e_PlayerRole_DM)
    builder.AddPlayer(-0.036, 0.1173, e_PlayerRole_RM)
    builder.AddPlayer(0.1907, -0.1973, e_PlayerRole_LM)
    builder.AddPlayer(0.28, 0.18, e_PlayerRole_RM)
    builder.AddPlayer(0.3773, 0.0147, e_PlayerRole_CF)
    builder.AddPlayer(0.42, -0.192, e_PlayerRole_CM)
    builder.AddPlayer(0.5493, 0.1707, e_PlayerRole_AM)
