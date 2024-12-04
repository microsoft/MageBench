
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
    builder.SetBallPosition(-0.0707, 0.1747)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9787, 0.008, e_PlayerRole_GK)
    builder.AddPlayer(-0.5573, 0.056, e_PlayerRole_CB)
    builder.AddPlayer(-0.4627, -0.1733, e_PlayerRole_LB)
    builder.AddPlayer(-0.4107, 0.2533, e_PlayerRole_RB)
    builder.AddPlayer(-0.3893, -0.0053, e_PlayerRole_DM)
    builder.AddPlayer(-0.3653, -0.1507, e_PlayerRole_LM)
    builder.AddPlayer(-0.096, -0.0213, e_PlayerRole_DM)
    builder.AddPlayer(-0.0893, -0.2613, e_PlayerRole_LM)
    builder.AddPlayer(-0.084, 0.1747, e_PlayerRole_AM)
    builder.AddPlayer(-0.0213, 0.384, e_PlayerRole_AM)
    builder.AddPlayer(0.2933, -0.132, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9787, -0.0053, e_PlayerRole_GK)
    builder.AddPlayer(-0.3013, 0.2173, e_PlayerRole_RB)
    builder.AddPlayer(-0.276, 0.0493, e_PlayerRole_RB)
    builder.AddPlayer(-0.204, -0.1493, e_PlayerRole_LB)
    builder.AddPlayer(0.036, -0.3307, e_PlayerRole_LM)
    builder.AddPlayer(0.072, 0.1987, e_PlayerRole_RM)
    builder.AddPlayer(0.0973, -0.028, e_PlayerRole_DM)
    builder.AddPlayer(0.2387, -0.2947, e_PlayerRole_LM)
    builder.AddPlayer(0.3333, 0.0707, e_PlayerRole_AM)
    builder.AddPlayer(0.3427, -0.224, e_PlayerRole_CM)
    builder.AddPlayer(0.4093, -0.088, e_PlayerRole_CF)
