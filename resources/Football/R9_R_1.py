
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
    builder.SetBallPosition(0.9893, 0.4053)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.98, 0.0053, e_PlayerRole_GK)
    builder.AddPlayer(0.1747, -0.0533, e_PlayerRole_LB)
    builder.AddPlayer(0.5053, 0.076, e_PlayerRole_CB)
    builder.AddPlayer(0.7453, -0.0107, e_PlayerRole_LB)
    builder.AddPlayer(0.7507, -0.0627, e_PlayerRole_LM)
    builder.AddPlayer(0.7533, 0.204, e_PlayerRole_DM)
    builder.AddPlayer(0.7773, -0.1227, e_PlayerRole_LM)
    builder.AddPlayer(0.844, -0.072, e_PlayerRole_LM)
    builder.AddPlayer(0.868, -0.028, e_PlayerRole_CM)
    builder.AddPlayer(0.944, 0.04, e_PlayerRole_CM)
    builder.AddPlayer(0.9933, 0.4093, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9733, 0.02, e_PlayerRole_GK)
    builder.AddPlayer(-0.9733, -0.0853, e_PlayerRole_LB)
    builder.AddPlayer(-0.9293, -0.0053, e_PlayerRole_CB)
    builder.AddPlayer(-0.9293, -0.0387, e_PlayerRole_CB)
    builder.AddPlayer(-0.9253, -0.144, e_PlayerRole_LM)
    builder.AddPlayer(-0.9027, 0.0213, e_PlayerRole_RM)
    builder.AddPlayer(-0.8867, 0.0267, e_PlayerRole_RM)
    builder.AddPlayer(-0.8627, 0.0613, e_PlayerRole_RM)
    builder.AddPlayer(-0.8027, 0.0973, e_PlayerRole_AM)
    builder.AddPlayer(-0.8, 0.0013, e_PlayerRole_CF)
    builder.AddPlayer(-0.7813, 0.048, e_PlayerRole_AM)
