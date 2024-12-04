
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
    builder.SetBallPosition(-0.812, 0.1533)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9667, -0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.856, 0.1307, e_PlayerRole_CB)
    builder.AddPlayer(-0.8053, 0.1533, e_PlayerRole_CB)
    builder.AddPlayer(-0.7813, -0.0493, e_PlayerRole_LB)
    builder.AddPlayer(-0.7427, 0.3107, e_PlayerRole_RM)
    builder.AddPlayer(-0.5147, 0.0333, e_PlayerRole_DM)
    builder.AddPlayer(-0.436, 0.3853, e_PlayerRole_RM)
    builder.AddPlayer(-0.224, -0.008, e_PlayerRole_DM)
    builder.AddPlayer(-0.1747, 0.1547, e_PlayerRole_CF)
    builder.AddPlayer(-0.1227, -0.24, e_PlayerRole_CM)
    builder.AddPlayer(0.0893, 0.0187, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9853, -0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.2427, 0.1493, e_PlayerRole_RB)
    builder.AddPlayer(-0.2227, -0.1133, e_PlayerRole_CB)
    builder.AddPlayer(0.1133, -0.0533, e_PlayerRole_CB)
    builder.AddPlayer(0.1507, 0.1227, e_PlayerRole_RM)
    builder.AddPlayer(0.1707, -0.2093, e_PlayerRole_LM)
    builder.AddPlayer(0.416, -0.34, e_PlayerRole_LM)
    builder.AddPlayer(0.4893, 0.0067, e_PlayerRole_RM)
    builder.AddPlayer(0.5507, -0.056, e_PlayerRole_CF)
    builder.AddPlayer(0.684, -0.192, e_PlayerRole_CM)
    builder.AddPlayer(0.88, -0.2907, e_PlayerRole_CM)
