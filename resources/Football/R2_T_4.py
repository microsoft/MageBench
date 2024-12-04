
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
    builder.SetBallPosition(-0.084, -0.3947)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9693, -0.0067, e_PlayerRole_GK)
    builder.AddPlayer(-0.5373, -0.076, e_PlayerRole_RB)
    builder.AddPlayer(-0.3653, -0.2613, e_PlayerRole_LB)
    builder.AddPlayer(-0.292, 0.0107, e_PlayerRole_RB)
    builder.AddPlayer(-0.252, -0.3627, e_PlayerRole_LM)
    builder.AddPlayer(-0.1947, -0.1947, e_PlayerRole_DM)
    builder.AddPlayer(-0.0947, -0.396, e_PlayerRole_LM)
    builder.AddPlayer(-0.0253, -0.1267, e_PlayerRole_DM)
    builder.AddPlayer(0.0733, -0.2747, e_PlayerRole_CM)
    builder.AddPlayer(0.2627, -0.0867, e_PlayerRole_AM)
    builder.AddPlayer(0.288, -0.3907, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9587, 0.024, e_PlayerRole_GK)
    builder.AddPlayer(-0.6533, 0.2227, e_PlayerRole_RB)
    builder.AddPlayer(-0.3213, 0.02, e_PlayerRole_LB)
    builder.AddPlayer(-0.2093, 0.2667, e_PlayerRole_RB)
    builder.AddPlayer(0.016, 0.3347, e_PlayerRole_RM)
    builder.AddPlayer(0.0773, 0.2373, e_PlayerRole_RM)
    builder.AddPlayer(0.1533, 0.296, e_PlayerRole_RM)
    builder.AddPlayer(0.2213, 0.336, e_PlayerRole_RM)
    builder.AddPlayer(0.2213, -0.0893, e_PlayerRole_CM)
    builder.AddPlayer(0.2307, 0.1453, e_PlayerRole_CF)
    builder.AddPlayer(0.4947, 0.0333, e_PlayerRole_CM)
