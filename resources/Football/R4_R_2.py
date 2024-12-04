
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
    builder.SetBallPosition(-0.84, -0.0987)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.984, -0.04, e_PlayerRole_GK)
    builder.AddPlayer(-0.936, -0.2787, e_PlayerRole_LB)
    builder.AddPlayer(-0.8973, -0.044, e_PlayerRole_RB)
    builder.AddPlayer(-0.8933, -0.0027, e_PlayerRole_RB)
    builder.AddPlayer(-0.848, -0.1027, e_PlayerRole_DM)
    builder.AddPlayer(-0.7547, -0.0373, e_PlayerRole_RM)
    builder.AddPlayer(-0.6893, -0.18, e_PlayerRole_LM)
    builder.AddPlayer(-0.6093, -0.244, e_PlayerRole_LM)
    builder.AddPlayer(-0.428, 0.0213, e_PlayerRole_AM)
    builder.AddPlayer(-0.3813, -0.1547, e_PlayerRole_CF)
    builder.AddPlayer(-0.2227, -0.224, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9613, 0.0067, e_PlayerRole_GK)
    builder.AddPlayer(-0.1307, 0.0347, e_PlayerRole_CB)
    builder.AddPlayer(-0.124, 0.2187, e_PlayerRole_RB)
    builder.AddPlayer(-0.1013, -0.26, e_PlayerRole_LB)
    builder.AddPlayer(0.0627, 0.3, e_PlayerRole_RM)
    builder.AddPlayer(0.1933, 0.128, e_PlayerRole_RM)
    builder.AddPlayer(0.2587, -0.036, e_PlayerRole_DM)
    builder.AddPlayer(0.6773, 0.2067, e_PlayerRole_RM)
    builder.AddPlayer(0.7507, 0.0107, e_PlayerRole_CF)
    builder.AddPlayer(0.7987, -0.048, e_PlayerRole_CF)
    builder.AddPlayer(0.9747, 0.3093, e_PlayerRole_AM)
