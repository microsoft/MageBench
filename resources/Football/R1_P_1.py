
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
    builder.SetBallPosition(-0.8107, -0.3507)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9813, -0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.9147, -0.072, e_PlayerRole_CB)
    builder.AddPlayer(-0.8347, -0.1813, e_PlayerRole_LB)
    builder.AddPlayer(-0.8307, -0.36, e_PlayerRole_LB)
    builder.AddPlayer(-0.8173, 0.096, e_PlayerRole_RM)
    builder.AddPlayer(-0.772, -0.16, e_PlayerRole_LM)
    builder.AddPlayer(-0.7013, 0.1773, e_PlayerRole_RM)
    builder.AddPlayer(-0.4693, 0.2493, e_PlayerRole_RM)
    builder.AddPlayer(-0.3707, 0.276, e_PlayerRole_AM)
    builder.AddPlayer(-0.272, -0.0627, e_PlayerRole_CF)
    builder.AddPlayer(-0.06, -0.1773, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.984, -0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.2253, -0.1173, e_PlayerRole_LB)
    builder.AddPlayer(0.1413, 0.228, e_PlayerRole_RB)
    builder.AddPlayer(0.3187, 0.132, e_PlayerRole_CB)
    builder.AddPlayer(0.4173, -0.0987, e_PlayerRole_LM)
    builder.AddPlayer(0.568, 0.0907, e_PlayerRole_DM)
    builder.AddPlayer(0.6093, 0.3347, e_PlayerRole_RM)
    builder.AddPlayer(0.704, -0.0267, e_PlayerRole_LM)
    builder.AddPlayer(0.7827, 0.2147, e_PlayerRole_AM)
    builder.AddPlayer(0.8307, 0.224, e_PlayerRole_AM)
    builder.AddPlayer(0.9413, 0.1707, e_PlayerRole_CF)
