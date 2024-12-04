
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
    builder.SetBallPosition(-0.82, 0.1027)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.932, 0.012, e_PlayerRole_GK)
    builder.AddPlayer(-0.928, 0.2547, e_PlayerRole_RB)
    builder.AddPlayer(-0.8467, -0.0133, e_PlayerRole_CB)
    builder.AddPlayer(-0.844, 0.0813, e_PlayerRole_RB)
    builder.AddPlayer(-0.828, 0.0867, e_PlayerRole_RM)
    builder.AddPlayer(-0.8253, -0.3, e_PlayerRole_LM)
    builder.AddPlayer(-0.7, 0.216, e_PlayerRole_RM)
    builder.AddPlayer(-0.6747, -0.084, e_PlayerRole_DM)
    builder.AddPlayer(-0.5067, -0.2587, e_PlayerRole_CM)
    builder.AddPlayer(-0.3173, 0.076, e_PlayerRole_AM)
    builder.AddPlayer(-0.1587, -0.0587, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9827, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.3267, -0.016, e_PlayerRole_CB)
    builder.AddPlayer(0.1333, -0.24, e_PlayerRole_LB)
    builder.AddPlayer(0.196, 0.048, e_PlayerRole_CB)
    builder.AddPlayer(0.368, -0.068, e_PlayerRole_DM)
    builder.AddPlayer(0.5427, 0.2253, e_PlayerRole_RM)
    builder.AddPlayer(0.6373, 0.0547, e_PlayerRole_RM)
    builder.AddPlayer(0.712, -0.1907, e_PlayerRole_LM)
    builder.AddPlayer(0.7667, 0.0293, e_PlayerRole_CF)
    builder.AddPlayer(0.888, -0.1133, e_PlayerRole_CF)
    builder.AddPlayer(0.888, -0.2933, e_PlayerRole_CM)
