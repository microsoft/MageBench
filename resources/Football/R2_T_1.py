
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
    builder.SetBallPosition(-0.1427, -0.332)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9627, 0.008, e_PlayerRole_GK)
    builder.AddPlayer(-0.4773, -0.168, e_PlayerRole_CB)
    builder.AddPlayer(-0.4667, 0.2187, e_PlayerRole_RB)
    builder.AddPlayer(-0.388, -0.34, e_PlayerRole_LB)
    builder.AddPlayer(-0.3373, -0.0093, e_PlayerRole_DM)
    builder.AddPlayer(-0.1507, -0.332, e_PlayerRole_LM)
    builder.AddPlayer(-0.076, -0.1987, e_PlayerRole_LM)
    builder.AddPlayer(0.084, -0.364, e_PlayerRole_LM)
    builder.AddPlayer(0.124, -0.1787, e_PlayerRole_CM)
    builder.AddPlayer(0.1533, 0.04, e_PlayerRole_AM)
    builder.AddPlayer(0.4213, -0.2627, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9627, -0.004, e_PlayerRole_GK)
    builder.AddPlayer(-0.4627, -0.2667, e_PlayerRole_LB)
    builder.AddPlayer(-0.368, 0.292, e_PlayerRole_RB)
    builder.AddPlayer(-0.336, 0.132, e_PlayerRole_CB)
    builder.AddPlayer(-0.072, 0.032, e_PlayerRole_DM)
    builder.AddPlayer(0.024, 0.288, e_PlayerRole_RM)
    builder.AddPlayer(0.248, 0.4053, e_PlayerRole_RM)
    builder.AddPlayer(0.312, 0.2347, e_PlayerRole_RM)
    builder.AddPlayer(0.392, -0.2533, e_PlayerRole_CM)
    builder.AddPlayer(0.3933, 0.0373, e_PlayerRole_CF)
    builder.AddPlayer(0.496, 0.1267, e_PlayerRole_CF)
