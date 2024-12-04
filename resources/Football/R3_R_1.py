
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
    builder.SetBallPosition(0.3493, -0.1627)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.98, 0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.224, 0.104, e_PlayerRole_RB)
    builder.AddPlayer(-0.0493, -0.2147, e_PlayerRole_LB)
    builder.AddPlayer(0.2987, 0.0533, e_PlayerRole_RB)
    builder.AddPlayer(0.3387, -0.168, e_PlayerRole_DM)
    builder.AddPlayer(0.3613, -0.2653, e_PlayerRole_LM)
    builder.AddPlayer(0.528, -0.2613, e_PlayerRole_LM)
    builder.AddPlayer(0.5667, -0.3853, e_PlayerRole_LM)
    builder.AddPlayer(0.6507, -0.0987, e_PlayerRole_CF)
    builder.AddPlayer(0.7347, 0.2547, e_PlayerRole_AM)
    builder.AddPlayer(0.796, -0.0053, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9747, -0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.8453, -0.056, e_PlayerRole_LB)
    builder.AddPlayer(-0.8293, 0.0227, e_PlayerRole_LB)
    builder.AddPlayer(-0.8253, 0.148, e_PlayerRole_CB)
    builder.AddPlayer(-0.772, 0.2787, e_PlayerRole_RM)
    builder.AddPlayer(-0.712, 0.0853, e_PlayerRole_DM)
    builder.AddPlayer(-0.5947, 0.28, e_PlayerRole_RM)
    builder.AddPlayer(-0.5573, 0.2373, e_PlayerRole_RM)
    builder.AddPlayer(-0.5413, 0.148, e_PlayerRole_CF)
    builder.AddPlayer(-0.0693, 0.1827, e_PlayerRole_AM)
    builder.AddPlayer(0.148, -0.0987, e_PlayerRole_CM)
