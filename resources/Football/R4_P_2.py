
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
    builder.SetBallPosition(-0.6813, 0.1093)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9867, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.8933, 0.0427, e_PlayerRole_CB)
    builder.AddPlayer(-0.8613, 0.236, e_PlayerRole_RB)
    builder.AddPlayer(-0.832, 0.0253, e_PlayerRole_CB)
    builder.AddPlayer(-0.8227, -0.0933, e_PlayerRole_DM)
    builder.AddPlayer(-0.812, -0.2707, e_PlayerRole_LM)
    builder.AddPlayer(-0.692, 0.1027, e_PlayerRole_RM)
    builder.AddPlayer(-0.6773, -0.0773, e_PlayerRole_DM)
    builder.AddPlayer(-0.656, 0.2533, e_PlayerRole_AM)
    builder.AddPlayer(-0.4667, 0.216, e_PlayerRole_AM)
    builder.AddPlayer(-0.196, -0.176, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.98, 0.0093, e_PlayerRole_GK)
    builder.AddPlayer(-0.2387, 0.0133, e_PlayerRole_RB)
    builder.AddPlayer(0.0907, -0.2587, e_PlayerRole_LB)
    builder.AddPlayer(0.1013, -0.0453, e_PlayerRole_CB)
    builder.AddPlayer(0.2293, 0.1467, e_PlayerRole_RM)
    builder.AddPlayer(0.4667, -0.0427, e_PlayerRole_DM)
    builder.AddPlayer(0.4933, -0.1987, e_PlayerRole_LM)
    builder.AddPlayer(0.6507, -0.2133, e_PlayerRole_LM)
    builder.AddPlayer(0.684, 0.0067, e_PlayerRole_CF)
    builder.AddPlayer(0.816, -0.0507, e_PlayerRole_CF)
    builder.AddPlayer(0.8333, -0.2107, e_PlayerRole_CM)
