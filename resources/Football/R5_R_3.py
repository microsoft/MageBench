
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
    builder.SetBallPosition(0.08, -0.0773)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.972, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.068, -0.1533, e_PlayerRole_CB)
    builder.AddPlayer(-0.0587, 0.008, e_PlayerRole_CB)
    builder.AddPlayer(0.0387, -0.232, e_PlayerRole_LB)
    builder.AddPlayer(0.084, -0.088, e_PlayerRole_DM)
    builder.AddPlayer(0.0987, 0.0947, e_PlayerRole_RM)
    builder.AddPlayer(0.3107, -0.28, e_PlayerRole_LM)
    builder.AddPlayer(0.3893, 0.0067, e_PlayerRole_DM)
    builder.AddPlayer(0.496, -0.3907, e_PlayerRole_CM)
    builder.AddPlayer(0.4987, 0.2813, e_PlayerRole_AM)
    builder.AddPlayer(0.732, 0.156, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9787, 0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.792, -0.2107, e_PlayerRole_LB)
    builder.AddPlayer(-0.784, 0.0587, e_PlayerRole_CB)
    builder.AddPlayer(-0.592, -0.0947, e_PlayerRole_LB)
    builder.AddPlayer(-0.5813, 0.2907, e_PlayerRole_RM)
    builder.AddPlayer(-0.572, 0.088, e_PlayerRole_DM)
    builder.AddPlayer(-0.4693, -0.0067, e_PlayerRole_DM)
    builder.AddPlayer(-0.384, 0.1293, e_PlayerRole_RM)
    builder.AddPlayer(-0.2733, 0.2293, e_PlayerRole_AM)
    builder.AddPlayer(-0.2, 0.1573, e_PlayerRole_AM)
    builder.AddPlayer(-0.1907, 0.04, e_PlayerRole_CF)
