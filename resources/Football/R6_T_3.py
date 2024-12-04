
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
    builder.SetBallPosition(0.808, -0.14)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9693, 0.0107, e_PlayerRole_GK)
    builder.AddPlayer(0.484, -0.1787, e_PlayerRole_LB)
    builder.AddPlayer(0.5667, -0.056, e_PlayerRole_CB)
    builder.AddPlayer(0.6947, -0.0173, e_PlayerRole_CB)
    builder.AddPlayer(0.696, -0.22, e_PlayerRole_LM)
    builder.AddPlayer(0.7027, 0.18, e_PlayerRole_RM)
    builder.AddPlayer(0.768, 0.32, e_PlayerRole_RM)
    builder.AddPlayer(0.8053, 0.0813, e_PlayerRole_DM)
    builder.AddPlayer(0.8107, -0.148, e_PlayerRole_CM)
    builder.AddPlayer(0.8133, -0.0333, e_PlayerRole_CF)
    builder.AddPlayer(0.8333, -0.3533, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9747, 0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.8693, -0.1773, e_PlayerRole_LB)
    builder.AddPlayer(-0.852, 0.3587, e_PlayerRole_RB)
    builder.AddPlayer(-0.788, -0.3333, e_PlayerRole_LB)
    builder.AddPlayer(-0.7493, 0.008, e_PlayerRole_DM)
    builder.AddPlayer(-0.7333, 0.1693, e_PlayerRole_RM)
    builder.AddPlayer(-0.7027, -0.1307, e_PlayerRole_LM)
    builder.AddPlayer(-0.6347, 0.132, e_PlayerRole_RM)
    builder.AddPlayer(-0.5813, -0.068, e_PlayerRole_CF)
    builder.AddPlayer(-0.5733, 0.3293, e_PlayerRole_AM)
    builder.AddPlayer(-0.4813, -0.2187, e_PlayerRole_CM)
