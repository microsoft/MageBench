
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
    builder.SetBallPosition(-0.3947, -0.1427)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.968, 0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.732, 0.016, e_PlayerRole_RB)
    builder.AddPlayer(-0.7253, -0.044, e_PlayerRole_RB)
    builder.AddPlayer(-0.7147, -0.2213, e_PlayerRole_LB)
    builder.AddPlayer(-0.7093, -0.1227, e_PlayerRole_DM)
    builder.AddPlayer(-0.668, -0.188, e_PlayerRole_LM)
    builder.AddPlayer(-0.6307, -0.0973, e_PlayerRole_DM)
    builder.AddPlayer(-0.5333, -0.0267, e_PlayerRole_RM)
    builder.AddPlayer(-0.4053, -0.1467, e_PlayerRole_CF)
    builder.AddPlayer(-0.2453, -0.268, e_PlayerRole_CM)
    builder.AddPlayer(0.2053, -0.1973, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9547, -0.0093, e_PlayerRole_GK)
    builder.AddPlayer(-0.3227, 0.02, e_PlayerRole_LB)
    builder.AddPlayer(0.2827, 0.0173, e_PlayerRole_LB)
    builder.AddPlayer(0.2987, 0.2093, e_PlayerRole_RB)
    builder.AddPlayer(0.408, 0.08, e_PlayerRole_DM)
    builder.AddPlayer(0.4587, 0.1733, e_PlayerRole_DM)
    builder.AddPlayer(0.4653, 0.356, e_PlayerRole_RM)
    builder.AddPlayer(0.496, 0.2493, e_PlayerRole_RM)
    builder.AddPlayer(0.5613, -0.0827, e_PlayerRole_CM)
    builder.AddPlayer(0.6987, 0.06, e_PlayerRole_CF)
    builder.AddPlayer(0.7667, -0.1, e_PlayerRole_CM)
