
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
    builder.SetBallPosition(0.5933, -0.3773)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9867, 0.004, e_PlayerRole_GK)
    builder.AddPlayer(0.276, -0.0907, e_PlayerRole_CB)
    builder.AddPlayer(0.3293, -0.2347, e_PlayerRole_LB)
    builder.AddPlayer(0.3613, 0.044, e_PlayerRole_CB)
    builder.AddPlayer(0.54, 0.196, e_PlayerRole_RM)
    builder.AddPlayer(0.5787, -0.38, e_PlayerRole_LM)
    builder.AddPlayer(0.66, 0.328, e_PlayerRole_RM)
    builder.AddPlayer(0.6613, -0.04, e_PlayerRole_DM)
    builder.AddPlayer(0.696, -0.1307, e_PlayerRole_CF)
    builder.AddPlayer(0.7307, 0.0547, e_PlayerRole_CF)
    builder.AddPlayer(0.892, 0.2573, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9853, -0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.8893, -0.2227, e_PlayerRole_LB)
    builder.AddPlayer(-0.8253, 0.188, e_PlayerRole_RB)
    builder.AddPlayer(-0.8093, -0.0947, e_PlayerRole_LB)
    builder.AddPlayer(-0.736, 0.076, e_PlayerRole_DM)
    builder.AddPlayer(-0.6853, 0.2667, e_PlayerRole_RM)
    builder.AddPlayer(-0.6613, -0.2747, e_PlayerRole_LM)
    builder.AddPlayer(-0.5613, -0.0987, e_PlayerRole_LM)
    builder.AddPlayer(-0.548, 0.1213, e_PlayerRole_AM)
    builder.AddPlayer(-0.5293, 0.3013, e_PlayerRole_AM)
    builder.AddPlayer(-0.3173, 0.1147, e_PlayerRole_AM)
