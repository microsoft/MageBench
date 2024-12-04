
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
    builder.SetBallPosition(0.416, -0.0467)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.984, -0.0067, e_PlayerRole_GK)
    builder.AddPlayer(0.1027, -0.0733, e_PlayerRole_CB)
    builder.AddPlayer(0.16, 0.224, e_PlayerRole_RB)
    builder.AddPlayer(0.212, -0.2267, e_PlayerRole_LB)
    builder.AddPlayer(0.3987, 0.2427, e_PlayerRole_RM)
    builder.AddPlayer(0.4053, -0.0453, e_PlayerRole_DM)
    builder.AddPlayer(0.5027, -0.3947, e_PlayerRole_LM)
    builder.AddPlayer(0.5627, -0.3027, e_PlayerRole_LM)
    builder.AddPlayer(0.5853, -0.1227, e_PlayerRole_CF)
    builder.AddPlayer(0.66, 0.072, e_PlayerRole_AM)
    builder.AddPlayer(0.7013, -0.3213, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9907, -0.0093, e_PlayerRole_GK)
    builder.AddPlayer(-0.764, -0.2707, e_PlayerRole_LB)
    builder.AddPlayer(-0.724, 0.3107, e_PlayerRole_RB)
    builder.AddPlayer(-0.5653, 0.3627, e_PlayerRole_RB)
    builder.AddPlayer(-0.5573, 0.0013, e_PlayerRole_DM)
    builder.AddPlayer(-0.5333, 0.288, e_PlayerRole_RM)
    builder.AddPlayer(-0.52, 0.0787, e_PlayerRole_DM)
    builder.AddPlayer(-0.5013, -0.2413, e_PlayerRole_LM)
    builder.AddPlayer(-0.2613, 0.26, e_PlayerRole_AM)
    builder.AddPlayer(-0.236, -0.1347, e_PlayerRole_CM)
    builder.AddPlayer(-0.196, 0.1, e_PlayerRole_CF)
