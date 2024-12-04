
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
    builder.SetBallPosition(0.06, -0.3907)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9707, 0.0093, e_PlayerRole_GK)
    builder.AddPlayer(-0.4013, -0.2947, e_PlayerRole_LB)
    builder.AddPlayer(-0.312, -0.108, e_PlayerRole_CB)
    builder.AddPlayer(-0.212, -0.3747, e_PlayerRole_LB)
    builder.AddPlayer(-0.1253, -0.252, e_PlayerRole_LM)
    builder.AddPlayer(-0.0707, -0.1533, e_PlayerRole_DM)
    builder.AddPlayer(0.0467, -0.3867, e_PlayerRole_LM)
    builder.AddPlayer(0.0747, 0.1933, e_PlayerRole_RM)
    builder.AddPlayer(0.2987, -0.2867, e_PlayerRole_CM)
    builder.AddPlayer(0.3253, -0.004, e_PlayerRole_CF)
    builder.AddPlayer(0.4627, -0.0507, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.944, 0.028, e_PlayerRole_GK)
    builder.AddPlayer(-0.6667, 0.2707, e_PlayerRole_RB)
    builder.AddPlayer(-0.528, -0.1227, e_PlayerRole_LB)
    builder.AddPlayer(-0.2853, -0.2187, e_PlayerRole_LB)
    builder.AddPlayer(-0.2613, 0.1347, e_PlayerRole_DM)
    builder.AddPlayer(-0.1773, 0.396, e_PlayerRole_RM)
    builder.AddPlayer(-0.1267, -0.2853, e_PlayerRole_LM)
    builder.AddPlayer(-0.0627, 0.284, e_PlayerRole_RM)
    builder.AddPlayer(0.1213, 0.396, e_PlayerRole_AM)
    builder.AddPlayer(0.184, 0.0533, e_PlayerRole_CF)
    builder.AddPlayer(0.336, 0.2053, e_PlayerRole_AM)
