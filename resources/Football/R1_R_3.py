
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
    builder.SetBallPosition(-0.5373, -0.3293)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9533, 0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.7213, -0.1987, e_PlayerRole_LB)
    builder.AddPlayer(-0.708, 0.2493, e_PlayerRole_RB)
    builder.AddPlayer(-0.6787, -0.0453, e_PlayerRole_CB)
    builder.AddPlayer(-0.5507, -0.3413, e_PlayerRole_LM)
    builder.AddPlayer(-0.3653, -0.3187, e_PlayerRole_LM)
    builder.AddPlayer(-0.324, -0.2013, e_PlayerRole_LM)
    builder.AddPlayer(-0.2, 0.0507, e_PlayerRole_DM)
    builder.AddPlayer(0.12, 0.1947, e_PlayerRole_AM)
    builder.AddPlayer(0.128, -0.0787, e_PlayerRole_CF)
    builder.AddPlayer(0.2227, -0.232, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9587, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.3333, -0.2693, e_PlayerRole_LB)
    builder.AddPlayer(-0.308, 0.0293, e_PlayerRole_CB)
    builder.AddPlayer(-0.2853, 0.2627, e_PlayerRole_RB)
    builder.AddPlayer(-0.0373, -0.0773, e_PlayerRole_LM)
    builder.AddPlayer(0.128, 0.2907, e_PlayerRole_RM)
    builder.AddPlayer(0.1373, 0.1813, e_PlayerRole_RM)
    builder.AddPlayer(0.2653, 0.3573, e_PlayerRole_RM)
    builder.AddPlayer(0.284, -0.0853, e_PlayerRole_CM)
    builder.AddPlayer(0.5467, 0.084, e_PlayerRole_CF)
    builder.AddPlayer(0.6733, 0.176, e_PlayerRole_AM)
