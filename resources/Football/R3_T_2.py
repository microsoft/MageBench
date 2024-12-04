
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
    builder.SetBallPosition(0.9813, -0.3827)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.988, 0.004, e_PlayerRole_GK)
    builder.AddPlayer(0.3427, 0.0907, e_PlayerRole_RB)
    builder.AddPlayer(0.5347, -0.0893, e_PlayerRole_CB)
    builder.AddPlayer(0.7533, -0.2613, e_PlayerRole_LB)
    builder.AddPlayer(0.788, 0.2093, e_PlayerRole_RM)
    builder.AddPlayer(0.8293, -0.0613, e_PlayerRole_DM)
    builder.AddPlayer(0.8307, 0.0787, e_PlayerRole_RM)
    builder.AddPlayer(0.8747, -0.0093, e_PlayerRole_DM)
    builder.AddPlayer(0.8827, -0.1693, e_PlayerRole_CF)
    builder.AddPlayer(0.9667, -0.1547, e_PlayerRole_CF)
    builder.AddPlayer(0.9907, -0.4, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9667, 0.0533, e_PlayerRole_GK)
    builder.AddPlayer(-0.952, -0.156, e_PlayerRole_LB)
    builder.AddPlayer(-0.912, 0.0827, e_PlayerRole_CB)
    builder.AddPlayer(-0.9107, -0.0573, e_PlayerRole_LB)
    builder.AddPlayer(-0.8627, -0.156, e_PlayerRole_LM)
    builder.AddPlayer(-0.8227, 0.2733, e_PlayerRole_RM)
    builder.AddPlayer(-0.8187, 0.148, e_PlayerRole_RM)
    builder.AddPlayer(-0.812, -0.0147, e_PlayerRole_LM)
    builder.AddPlayer(-0.756, -0.124, e_PlayerRole_CM)
    builder.AddPlayer(-0.7013, 0.1813, e_PlayerRole_AM)
    builder.AddPlayer(-0.5547, 0.1253, e_PlayerRole_CF)
