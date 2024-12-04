
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
    builder.SetBallPosition(-0.0467, 0.2973)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9827, 0.0053, e_PlayerRole_GK)
    builder.AddPlayer(-0.776, 0.1507, e_PlayerRole_CB)
    builder.AddPlayer(-0.6667, -0.16, e_PlayerRole_LB)
    builder.AddPlayer(-0.5093, 0.0213, e_PlayerRole_LB)
    builder.AddPlayer(-0.4773, 0.2533, e_PlayerRole_RM)
    builder.AddPlayer(-0.292, 0.4, e_PlayerRole_RM)
    builder.AddPlayer(-0.2693, 0.1507, e_PlayerRole_DM)
    builder.AddPlayer(-0.2573, 0.3707, e_PlayerRole_RM)
    builder.AddPlayer(-0.0547, 0.3067, e_PlayerRole_AM)
    builder.AddPlayer(-0.0187, 0.112, e_PlayerRole_CF)
    builder.AddPlayer(0.128, 0.4067, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.984, -0.0053, e_PlayerRole_GK)
    builder.AddPlayer(-0.612, -0.2747, e_PlayerRole_LB)
    builder.AddPlayer(-0.5667, -0.048, e_PlayerRole_RB)
    builder.AddPlayer(-0.424, 0.1133, e_PlayerRole_RB)
    builder.AddPlayer(-0.332, -0.1387, e_PlayerRole_DM)
    builder.AddPlayer(-0.18, -0.3947, e_PlayerRole_LM)
    builder.AddPlayer(-0.0987, 0.0947, e_PlayerRole_RM)
    builder.AddPlayer(0.0147, -0.1507, e_PlayerRole_DM)
    builder.AddPlayer(0.2147, -0.1587, e_PlayerRole_CF)
    builder.AddPlayer(0.224, -0.3813, e_PlayerRole_CM)
    builder.AddPlayer(0.444, -0.2427, e_PlayerRole_CM)
