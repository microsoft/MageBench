
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
    builder.SetBallPosition(0.5387, 0.3867)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9587, -0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.388, 0.1413, e_PlayerRole_CB)
    builder.AddPlayer(-0.3013, -0.1387, e_PlayerRole_LB)
    builder.AddPlayer(-0.2893, -0.2547, e_PlayerRole_LB)
    builder.AddPlayer(-0.2307, -0.028, e_PlayerRole_DM)
    builder.AddPlayer(-0.212, 0.1747, e_PlayerRole_RM)
    builder.AddPlayer(0.1573, 0.3067, e_PlayerRole_RM)
    builder.AddPlayer(0.2067, -0.1693, e_PlayerRole_LM)
    builder.AddPlayer(0.4907, -0.068, e_PlayerRole_CM)
    builder.AddPlayer(0.548, 0.384, e_PlayerRole_AM)
    builder.AddPlayer(0.632, 0.1053, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9707, -0.008, e_PlayerRole_GK)
    builder.AddPlayer(-0.7027, -0.1907, e_PlayerRole_LB)
    builder.AddPlayer(-0.6493, 0.0267, e_PlayerRole_CB)
    builder.AddPlayer(-0.58, -0.3107, e_PlayerRole_LB)
    builder.AddPlayer(-0.5307, 0.0933, e_PlayerRole_RM)
    builder.AddPlayer(-0.484, 0.1747, e_PlayerRole_RM)
    builder.AddPlayer(-0.3813, -0.1213, e_PlayerRole_DM)
    builder.AddPlayer(-0.3027, 0.0947, e_PlayerRole_RM)
    builder.AddPlayer(-0.0427, -0.1467, e_PlayerRole_CM)
    builder.AddPlayer(0.0867, 0.0227, e_PlayerRole_CF)
    builder.AddPlayer(0.1627, 0.2027, e_PlayerRole_AM)
