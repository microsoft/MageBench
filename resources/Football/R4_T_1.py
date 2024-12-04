
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
    builder.SetBallPosition(-0.824, 0.0587)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9613, -0.0133, e_PlayerRole_GK)
    builder.AddPlayer(-0.8547, 0.2973, e_PlayerRole_RB)
    builder.AddPlayer(-0.8307, -0.132, e_PlayerRole_LB)
    builder.AddPlayer(-0.8173, 0.0693, e_PlayerRole_CB)
    builder.AddPlayer(-0.664, 0.0293, e_PlayerRole_DM)
    builder.AddPlayer(-0.6453, 0.2533, e_PlayerRole_RM)
    builder.AddPlayer(-0.6187, -0.06, e_PlayerRole_DM)
    builder.AddPlayer(-0.5013, -0.264, e_PlayerRole_LM)
    builder.AddPlayer(-0.408, 0.2013, e_PlayerRole_AM)
    builder.AddPlayer(-0.2693, 0.0293, e_PlayerRole_CF)
    builder.AddPlayer(-0.2293, -0.172, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.964, -0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.6693, -0.096, e_PlayerRole_LB)
    builder.AddPlayer(-0.4093, 0.1653, e_PlayerRole_RB)
    builder.AddPlayer(-0.2, -0.1707, e_PlayerRole_LB)
    builder.AddPlayer(0.0693, 0.144, e_PlayerRole_RM)
    builder.AddPlayer(0.0827, -0.0267, e_PlayerRole_DM)
    builder.AddPlayer(0.1373, -0.1893, e_PlayerRole_LM)
    builder.AddPlayer(0.396, 0.2333, e_PlayerRole_RM)
    builder.AddPlayer(0.5467, -0.0293, e_PlayerRole_CF)
    builder.AddPlayer(0.684, -0.156, e_PlayerRole_CM)
    builder.AddPlayer(0.776, 0.08, e_PlayerRole_CF)
