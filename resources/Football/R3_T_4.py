
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
    builder.SetBallPosition(0.96, -0.26)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9733, 0.0027, e_PlayerRole_GK)
    builder.AddPlayer(0.3, 0.2187, e_PlayerRole_RB)
    builder.AddPlayer(0.3147, -0.2053, e_PlayerRole_LB)
    builder.AddPlayer(0.332, -0.0187, e_PlayerRole_CB)
    builder.AddPlayer(0.508, -0.04, e_PlayerRole_DM)
    builder.AddPlayer(0.5893, 0.1373, e_PlayerRole_RM)
    builder.AddPlayer(0.6507, -0.2307, e_PlayerRole_LM)
    builder.AddPlayer(0.6947, 0.2267, e_PlayerRole_RM)
    builder.AddPlayer(0.82, -0.092, e_PlayerRole_CF)
    builder.AddPlayer(0.86, 0.152, e_PlayerRole_AM)
    builder.AddPlayer(0.96, -0.272, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9733, 0.0333, e_PlayerRole_GK)
    builder.AddPlayer(-0.9227, 0.3413, e_PlayerRole_RB)
    builder.AddPlayer(-0.9147, -0.0667, e_PlayerRole_LB)
    builder.AddPlayer(-0.828, 0.2, e_PlayerRole_RB)
    builder.AddPlayer(-0.8253, 0.3333, e_PlayerRole_RM)
    builder.AddPlayer(-0.808, -0.0067, e_PlayerRole_DM)
    builder.AddPlayer(-0.7507, -0.2827, e_PlayerRole_LM)
    builder.AddPlayer(-0.7333, 0.3893, e_PlayerRole_RM)
    builder.AddPlayer(-0.636, -0.1147, e_PlayerRole_CM)
    builder.AddPlayer(-0.4947, -0.252, e_PlayerRole_CM)
    builder.AddPlayer(-0.3987, -0.032, e_PlayerRole_CF)
