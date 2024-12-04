
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
    builder.SetBallPosition(-0.812, -0.372)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.932, -0.0307, e_PlayerRole_GK)
    builder.AddPlayer(-0.884, -0.176, e_PlayerRole_CB)
    builder.AddPlayer(-0.824, -0.3813, e_PlayerRole_LB)
    builder.AddPlayer(-0.744, -0.192, e_PlayerRole_CB)
    builder.AddPlayer(-0.6, -0.3627, e_PlayerRole_LM)
    builder.AddPlayer(-0.5227, 0.1467, e_PlayerRole_RM)
    builder.AddPlayer(-0.4707, -0.232, e_PlayerRole_LM)
    builder.AddPlayer(-0.3333, -0.0907, e_PlayerRole_DM)
    builder.AddPlayer(-0.1867, -0.3427, e_PlayerRole_CM)
    builder.AddPlayer(-0.1493, 0.132, e_PlayerRole_AM)
    builder.AddPlayer(0.1467, -0.1147, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9613, -0.0053, e_PlayerRole_GK)
    builder.AddPlayer(-0.524, -0.2027, e_PlayerRole_LB)
    builder.AddPlayer(-0.332, 0.112, e_PlayerRole_CB)
    builder.AddPlayer(-0.1053, 0.3267, e_PlayerRole_RB)
    builder.AddPlayer(-0.0893, -0.1947, e_PlayerRole_LM)
    builder.AddPlayer(0.092, -0.048, e_PlayerRole_LM)
    builder.AddPlayer(0.232, 0.232, e_PlayerRole_RM)
    builder.AddPlayer(0.3573, -0.0907, e_PlayerRole_LM)
    builder.AddPlayer(0.4827, 0.1053, e_PlayerRole_CF)
    builder.AddPlayer(0.7613, 0.3187, e_PlayerRole_AM)
    builder.AddPlayer(0.8027, 0.1547, e_PlayerRole_AM)
