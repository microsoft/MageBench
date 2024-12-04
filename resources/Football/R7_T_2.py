
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
    builder.SetBallPosition(-0.844, 0.1413)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9733, 0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.904, -0.2573, e_PlayerRole_LB)
    builder.AddPlayer(-0.848, 0.152, e_PlayerRole_RB)
    builder.AddPlayer(-0.8187, -0.104, e_PlayerRole_LB)
    builder.AddPlayer(-0.7947, 0.3053, e_PlayerRole_RM)
    builder.AddPlayer(-0.6787, -0.1733, e_PlayerRole_LM)
    builder.AddPlayer(-0.6133, 0.1587, e_PlayerRole_RM)
    builder.AddPlayer(-0.604, -0.3, e_PlayerRole_LM)
    builder.AddPlayer(-0.2613, -0.172, e_PlayerRole_CM)
    builder.AddPlayer(-0.1467, 0.2227, e_PlayerRole_AM)
    builder.AddPlayer(0.38, -0.0093, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.964, -0.008, e_PlayerRole_GK)
    builder.AddPlayer(-0.436, -0.0227, e_PlayerRole_CB)
    builder.AddPlayer(-0.272, 0.2427, e_PlayerRole_RB)
    builder.AddPlayer(0.1, -0.0827, e_PlayerRole_CB)
    builder.AddPlayer(0.1667, 0.248, e_PlayerRole_RM)
    builder.AddPlayer(0.2067, -0.276, e_PlayerRole_LM)
    builder.AddPlayer(0.3867, -0.048, e_PlayerRole_DM)
    builder.AddPlayer(0.4107, 0.1227, e_PlayerRole_RM)
    builder.AddPlayer(0.652, -0.228, e_PlayerRole_CM)
    builder.AddPlayer(0.7213, -0.0813, e_PlayerRole_CF)
    builder.AddPlayer(0.8107, -0.3427, e_PlayerRole_CM)
