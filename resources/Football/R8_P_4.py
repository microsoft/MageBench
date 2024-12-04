
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
    builder.SetBallPosition(-0.0533, 0.208)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.992, 0.0053, e_PlayerRole_GK)
    builder.AddPlayer(-0.7027, -0.056, e_PlayerRole_LB)
    builder.AddPlayer(-0.3173, 0.2067, e_PlayerRole_CB)
    builder.AddPlayer(-0.2267, 0.2987, e_PlayerRole_RB)
    builder.AddPlayer(-0.1747, 0.0453, e_PlayerRole_LM)
    builder.AddPlayer(-0.088, -0.0227, e_PlayerRole_LM)
    builder.AddPlayer(-0.0733, 0.0227, e_PlayerRole_LM)
    builder.AddPlayer(-0.068, 0.2053, e_PlayerRole_DM)
    builder.AddPlayer(0.0893, -0.0093, e_PlayerRole_CM)
    builder.AddPlayer(0.292, 0.3853, e_PlayerRole_AM)
    builder.AddPlayer(0.5533, -0.1133, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9867, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.6427, -0.184, e_PlayerRole_CB)
    builder.AddPlayer(-0.5387, 0.0747, e_PlayerRole_RB)
    builder.AddPlayer(-0.244, -0.3587, e_PlayerRole_LB)
    builder.AddPlayer(-0.168, -0.196, e_PlayerRole_DM)
    builder.AddPlayer(-0.1213, -0.032, e_PlayerRole_RM)
    builder.AddPlayer(0.0573, -0.0533, e_PlayerRole_RM)
    builder.AddPlayer(0.192, -0.072, e_PlayerRole_DM)
    builder.AddPlayer(0.1933, -0.2853, e_PlayerRole_CM)
    builder.AddPlayer(0.2253, -0.2693, e_PlayerRole_CM)
    builder.AddPlayer(0.2547, -0.2067, e_PlayerRole_CF)
