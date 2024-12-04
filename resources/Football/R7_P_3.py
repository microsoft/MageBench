
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
    builder.SetBallPosition(-0.6107, 0.2613)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9773, 0.0093, e_PlayerRole_GK)
    builder.AddPlayer(-0.8453, 0.2827, e_PlayerRole_RB)
    builder.AddPlayer(-0.76, 0.384, e_PlayerRole_RB)
    builder.AddPlayer(-0.7333, 0.136, e_PlayerRole_CB)
    builder.AddPlayer(-0.6253, 0.2627, e_PlayerRole_RB)
    builder.AddPlayer(-0.5867, 0.08, e_PlayerRole_DM)
    builder.AddPlayer(-0.4387, 0.12, e_PlayerRole_DM)
    builder.AddPlayer(-0.3267, -0.092, e_PlayerRole_LM)
    builder.AddPlayer(-0.1387, -0.1, e_PlayerRole_LM)
    builder.AddPlayer(-0.0653, 0.0507, e_PlayerRole_CF)
    builder.AddPlayer(0.0333, -0.116, e_PlayerRole_CM)

    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9813, 0.0107, e_PlayerRole_GK)
    builder.AddPlayer(-0.2707, 0.0413, e_PlayerRole_RB)
    builder.AddPlayer(0.0947, -0.1, e_PlayerRole_CB)
    builder.AddPlayer(0.1093, 0.0667, e_PlayerRole_RB)
    builder.AddPlayer(0.2507, 0.0387, e_PlayerRole_RM)
    builder.AddPlayer(0.3533, -0.244, e_PlayerRole_LM)
    builder.AddPlayer(0.4747, -0.164, e_PlayerRole_DM)
    builder.AddPlayer(0.6013, -0.1267, e_PlayerRole_DM)
    builder.AddPlayer(0.6853, -0.368, e_PlayerRole_CM)
    builder.AddPlayer(0.7213, -0.148, e_PlayerRole_CF)
    builder.AddPlayer(0.804, -0.28, e_PlayerRole_CM)
