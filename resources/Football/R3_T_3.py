
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
    builder.SetBallPosition(0.968, -0.2893)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.988, 0.0, e_PlayerRole_GK)
    builder.AddPlayer(0.2467, -0.164, e_PlayerRole_LB)
    builder.AddPlayer(0.2933, 0.052, e_PlayerRole_RB)
    builder.AddPlayer(0.472, -0.2453, e_PlayerRole_LB)
    builder.AddPlayer(0.572, 0.164, e_PlayerRole_RM)
    builder.AddPlayer(0.648, -0.0853, e_PlayerRole_DM)
    builder.AddPlayer(0.764, -0.088, e_PlayerRole_DM)
    builder.AddPlayer(0.7733, 0.0613, e_PlayerRole_RM)
    builder.AddPlayer(0.8533, -0.2027, e_PlayerRole_CM)
    builder.AddPlayer(0.8813, 0.1987, e_PlayerRole_AM)
    builder.AddPlayer(0.964, -0.308, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9827, 0.0067, e_PlayerRole_GK)
    builder.AddPlayer(-0.98, 0.168, e_PlayerRole_RB)
    builder.AddPlayer(-0.952, -0.24, e_PlayerRole_LB)
    builder.AddPlayer(-0.856, 0.3667, e_PlayerRole_RB)
    builder.AddPlayer(-0.84, 0.1413, e_PlayerRole_DM)
    builder.AddPlayer(-0.8387, 0.304, e_PlayerRole_RM)
    builder.AddPlayer(-0.772, -0.2053, e_PlayerRole_LM)
    builder.AddPlayer(-0.704, 0.028, e_PlayerRole_DM)
    builder.AddPlayer(-0.5187, -0.112, e_PlayerRole_CM)
    builder.AddPlayer(-0.4293, 0.088, e_PlayerRole_CF)
    builder.AddPlayer(-0.3893, 0.008, e_PlayerRole_CF)
