
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
    builder.SetBallPosition(0.9093, 0.2987)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9613, 0.0053, e_PlayerRole_GK)
    builder.AddPlayer(0.0413, 0.1933, e_PlayerRole_RB)
    builder.AddPlayer(0.1027, 0.0973, e_PlayerRole_CB)
    builder.AddPlayer(0.1907, -0.2227, e_PlayerRole_LM)
    builder.AddPlayer(0.4347, 0.036, e_PlayerRole_DM)
    builder.AddPlayer(0.5093, 0.1253, e_PlayerRole_DM)
    builder.AddPlayer(0.516, -0.212, e_PlayerRole_LM)
    builder.AddPlayer(0.5187, 0.3533, e_PlayerRole_AM)
    builder.AddPlayer(0.7507, 0.344, e_PlayerRole_AM)
    builder.AddPlayer(0.7867, 0.0013, e_PlayerRole_CF)
    builder.AddPlayer(0.9, 0.2987, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.976, -0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.8973, -0.22, e_PlayerRole_LB)
    builder.AddPlayer(-0.876, -0.0093, e_PlayerRole_CB)
    builder.AddPlayer(-0.8067, -0.2773, e_PlayerRole_LB)
    builder.AddPlayer(-0.7547, -0.072, e_PlayerRole_DM)
    builder.AddPlayer(-0.7547, 0.084, e_PlayerRole_RM)
    builder.AddPlayer(-0.676, -0.2133, e_PlayerRole_LM)
    builder.AddPlayer(-0.6187, 0.1867, e_PlayerRole_RM)
    builder.AddPlayer(-0.5933, -0.2747, e_PlayerRole_CM)
    builder.AddPlayer(-0.3707, 0.0053, e_PlayerRole_CF)
    builder.AddPlayer(-0.1253, -0.0987, e_PlayerRole_CF)
