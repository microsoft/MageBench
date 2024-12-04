
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
    builder.SetBallPosition(-0.8987, 0.016)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9067, 0.0093, e_PlayerRole_GK)
    builder.AddPlayer(-0.724, 0.1253, e_PlayerRole_RB)
    builder.AddPlayer(-0.4573, -0.1173, e_PlayerRole_LB)
    builder.AddPlayer(-0.4453, 0.352, e_PlayerRole_RB)
    builder.AddPlayer(-0.424, -0.0467, e_PlayerRole_DM)
    builder.AddPlayer(-0.188, -0.164, e_PlayerRole_LM)
    builder.AddPlayer(-0.1693, -0.3107, e_PlayerRole_LM)
    builder.AddPlayer(-0.08, -0.0293, e_PlayerRole_DM)
    builder.AddPlayer(0.0627, 0.22, e_PlayerRole_AM)
    builder.AddPlayer(0.3, -0.3507, e_PlayerRole_CM)
    builder.AddPlayer(0.38, 0.272, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.98, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.52, -0.0013, e_PlayerRole_CB)
    builder.AddPlayer(-0.46, 0.196, e_PlayerRole_RB)
    builder.AddPlayer(-0.4427, -0.192, e_PlayerRole_LB)
    builder.AddPlayer(-0.248, 0.0613, e_PlayerRole_RM)
    builder.AddPlayer(-0.228, 0.172, e_PlayerRole_RM)
    builder.AddPlayer(0.0213, 0.092, e_PlayerRole_RM)
    builder.AddPlayer(0.1733, -0.0253, e_PlayerRole_DM)
    builder.AddPlayer(0.2387, -0.2907, e_PlayerRole_CM)
    builder.AddPlayer(0.3733, 0.1587, e_PlayerRole_AM)
    builder.AddPlayer(0.7013, -0.0493, e_PlayerRole_CF)
