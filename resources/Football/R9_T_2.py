
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
    builder.SetBallPosition(0.9867, 0.4027)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9827, 0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.104, -0.0093, e_PlayerRole_LB)
    builder.AddPlayer(0.592, 0.256, e_PlayerRole_RB)
    builder.AddPlayer(0.6267, 0.1627, e_PlayerRole_CB)
    builder.AddPlayer(0.6787, -0.0027, e_PlayerRole_LM)
    builder.AddPlayer(0.7493, -0.1573, e_PlayerRole_LM)
    builder.AddPlayer(0.8173, 0.1227, e_PlayerRole_DM)
    builder.AddPlayer(0.8347, -0.0493, e_PlayerRole_LM)
    builder.AddPlayer(0.8413, 0.06, e_PlayerRole_CF)
    builder.AddPlayer(0.9147, 0.308, e_PlayerRole_AM)
    builder.AddPlayer(0.9907, 0.412, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9707, -0.0533, e_PlayerRole_GK)
    builder.AddPlayer(-0.936, -0.1613, e_PlayerRole_LB)
    builder.AddPlayer(-0.8973, 0.016, e_PlayerRole_CB)
    builder.AddPlayer(-0.8453, -0.116, e_PlayerRole_LB)
    builder.AddPlayer(-0.8307, -0.012, e_PlayerRole_DM)
    builder.AddPlayer(-0.8013, 0.124, e_PlayerRole_RM)
    builder.AddPlayer(-0.7867, -0.0787, e_PlayerRole_LM)
    builder.AddPlayer(-0.688, -0.06, e_PlayerRole_DM)
    builder.AddPlayer(-0.576, -0.1733, e_PlayerRole_CM)
    builder.AddPlayer(-0.5653, 0.06, e_PlayerRole_AM)
    builder.AddPlayer(-0.0587, -0.0107, e_PlayerRole_CF)
