
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
    builder.SetBallPosition(-0.9173, -0.0267)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.928, -0.032, e_PlayerRole_GK)
    builder.AddPlayer(-0.4653, -0.1947, e_PlayerRole_LB)
    builder.AddPlayer(-0.3253, 0.1973, e_PlayerRole_RB)
    builder.AddPlayer(-0.3227, -0.044, e_PlayerRole_CB)
    builder.AddPlayer(-0.1067, -0.18, e_PlayerRole_LM)
    builder.AddPlayer(-0.0773, 0.0733, e_PlayerRole_RM)
    builder.AddPlayer(-0.072, -0.0467, e_PlayerRole_DM)
    builder.AddPlayer(0.1253, -0.0947, e_PlayerRole_LM)
    builder.AddPlayer(0.152, 0.036, e_PlayerRole_CF)
    builder.AddPlayer(0.3093, -0.22, e_PlayerRole_CM)
    builder.AddPlayer(0.364, 0.1413, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9853, -0.0, e_PlayerRole_GK)
    builder.AddPlayer(-0.2733, 0.1, e_PlayerRole_RB)
    builder.AddPlayer(-0.1067, -0.0533, e_PlayerRole_CB)
    builder.AddPlayer(-0.0973, 0.0547, e_PlayerRole_CB)
    builder.AddPlayer(0.1173, 0.028, e_PlayerRole_DM)
    builder.AddPlayer(0.14, 0.144, e_PlayerRole_RM)
    builder.AddPlayer(0.4013, -0.1933, e_PlayerRole_LM)
    builder.AddPlayer(0.444, 0.016, e_PlayerRole_DM)
    builder.AddPlayer(0.5147, 0.1787, e_PlayerRole_AM)
    builder.AddPlayer(0.616, 0.2067, e_PlayerRole_AM)
    builder.AddPlayer(0.7533, 0.0427, e_PlayerRole_CF)
