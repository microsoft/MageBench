
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
    builder.SetBallPosition(-0.748, -0.1187)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9227, -0.032, e_PlayerRole_GK)
    builder.AddPlayer(-0.8107, -0.252, e_PlayerRole_LB)
    builder.AddPlayer(-0.7893, 0.2587, e_PlayerRole_RB)
    builder.AddPlayer(-0.7533, -0.1307, e_PlayerRole_LB)
    builder.AddPlayer(-0.7307, 0.116, e_PlayerRole_RM)
    builder.AddPlayer(-0.5733, 0.0187, e_PlayerRole_DM)
    builder.AddPlayer(-0.5507, -0.272, e_PlayerRole_LM)
    builder.AddPlayer(-0.3853, 0.2093, e_PlayerRole_RM)
    builder.AddPlayer(-0.3347, 0.0107, e_PlayerRole_CF)
    builder.AddPlayer(-0.0787, -0.3013, e_PlayerRole_CM)
    builder.AddPlayer(0.156, 0.1507, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.968, 0.008, e_PlayerRole_GK)
    builder.AddPlayer(-0.5027, -0.232, e_PlayerRole_LB)
    builder.AddPlayer(-0.4827, 0.0133, e_PlayerRole_CB)
    builder.AddPlayer(-0.3213, 0.1067, e_PlayerRole_RB)
    builder.AddPlayer(-0.1533, -0.1147, e_PlayerRole_DM)
    builder.AddPlayer(0.124, -0.3293, e_PlayerRole_LM)
    builder.AddPlayer(0.1507, 0.3053, e_PlayerRole_RM)
    builder.AddPlayer(0.196, -0.152, e_PlayerRole_LM)
    builder.AddPlayer(0.2187, 0.1707, e_PlayerRole_AM)
    builder.AddPlayer(0.4947, -0.0, e_PlayerRole_CF)
    builder.AddPlayer(0.6413, 0.1973, e_PlayerRole_AM)
