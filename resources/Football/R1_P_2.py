
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
    builder.SetBallPosition(-0.712, -0.3987)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9773, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.836, -0.2227, e_PlayerRole_LB)
    builder.AddPlayer(-0.736, -0.3973, e_PlayerRole_LB)
    builder.AddPlayer(-0.6987, -0.1027, e_PlayerRole_CB)
    builder.AddPlayer(-0.684, -0.2453, e_PlayerRole_LM)
    builder.AddPlayer(-0.632, 0.2187, e_PlayerRole_RM)
    builder.AddPlayer(-0.3733, -0.32, e_PlayerRole_LM)
    builder.AddPlayer(-0.256, 0.104, e_PlayerRole_RM)
    builder.AddPlayer(-0.0853, 0.28, e_PlayerRole_AM)
    builder.AddPlayer(-0.08, -0.0107, e_PlayerRole_CF)
    builder.AddPlayer(0.028, -0.1333, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.972, 0.0067, e_PlayerRole_GK)
    builder.AddPlayer(-0.1787, 0.1413, e_PlayerRole_RB)
    builder.AddPlayer(0.104, 0.08, e_PlayerRole_CB)
    builder.AddPlayer(0.1053, -0.3293, e_PlayerRole_LB)
    builder.AddPlayer(0.3067, -0.0013, e_PlayerRole_DM)
    builder.AddPlayer(0.42, 0.3693, e_PlayerRole_RM)
    builder.AddPlayer(0.464, 0.076, e_PlayerRole_DM)
    builder.AddPlayer(0.6653, -0.176, e_PlayerRole_LM)
    builder.AddPlayer(0.6947, 0.1627, e_PlayerRole_AM)
    builder.AddPlayer(0.7053, 0.3053, e_PlayerRole_AM)
    builder.AddPlayer(0.8307, 0.2787, e_PlayerRole_AM)
