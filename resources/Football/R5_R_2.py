
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
    builder.SetBallPosition(0.0413, -0.0213)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9707, -0.0067, e_PlayerRole_GK)
    builder.AddPlayer(-0.3507, 0.1387, e_PlayerRole_RB)
    builder.AddPlayer(-0.292, -0.252, e_PlayerRole_LB)
    builder.AddPlayer(-0.1933, 0.0093, e_PlayerRole_RB)
    builder.AddPlayer(-0.152, -0.1973, e_PlayerRole_LM)
    builder.AddPlayer(0.032, -0.016, e_PlayerRole_DM)
    builder.AddPlayer(0.0613, 0.1547, e_PlayerRole_RM)
    builder.AddPlayer(0.092, -0.336, e_PlayerRole_LM)
    builder.AddPlayer(0.124, -0.132, e_PlayerRole_CF)
    builder.AddPlayer(0.3853, -0.1973, e_PlayerRole_CM)
    builder.AddPlayer(0.3853, 0.0853, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9667, -0.0053, e_PlayerRole_GK)
    builder.AddPlayer(-0.5147, 0.0493, e_PlayerRole_CB)
    builder.AddPlayer(-0.512, 0.1747, e_PlayerRole_RB)
    builder.AddPlayer(-0.5093, 0.3133, e_PlayerRole_RB)
    builder.AddPlayer(-0.4947, -0.1493, e_PlayerRole_LM)
    builder.AddPlayer(-0.4293, 0.0947, e_PlayerRole_DM)
    builder.AddPlayer(-0.3133, 0.2573, e_PlayerRole_RM)
    builder.AddPlayer(-0.1987, 0.0533, e_PlayerRole_DM)
    builder.AddPlayer(-0.096, -0.0987, e_PlayerRole_CM)
    builder.AddPlayer(-0.072, 0.1707, e_PlayerRole_AM)
    builder.AddPlayer(0.1027, -0.0533, e_PlayerRole_CM)
