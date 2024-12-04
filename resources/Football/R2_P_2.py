
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
    builder.SetBallPosition(-0.1, -0.304)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9773, 0.008, e_PlayerRole_GK)
    builder.AddPlayer(-0.5453, -0.1147, e_PlayerRole_CB)
    builder.AddPlayer(-0.5133, 0.0107, e_PlayerRole_RB)
    builder.AddPlayer(-0.384, -0.2813, e_PlayerRole_LB)
    builder.AddPlayer(-0.3093, -0.08, e_PlayerRole_RM)
    builder.AddPlayer(-0.2867, -0.3613, e_PlayerRole_LM)
    builder.AddPlayer(-0.2827, 0.056, e_PlayerRole_RM)
    builder.AddPlayer(-0.1107, -0.1733, e_PlayerRole_DM)
    builder.AddPlayer(-0.104, -0.2907, e_PlayerRole_CM)
    builder.AddPlayer(0.0493, -0.0853, e_PlayerRole_CF)
    builder.AddPlayer(0.2387, -0.1107, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.988, -0.0, e_PlayerRole_GK)
    builder.AddPlayer(-0.3187, 0.1067, e_PlayerRole_CB)
    builder.AddPlayer(-0.2853, 0.028, e_PlayerRole_LB)
    builder.AddPlayer(-0.184, -0.0733, e_PlayerRole_LB)
    builder.AddPlayer(-0.152, 0.16, e_PlayerRole_DM)
    builder.AddPlayer(-0.044, 0.148, e_PlayerRole_DM)
    builder.AddPlayer(-0.036, 0.352, e_PlayerRole_RM)
    builder.AddPlayer(0.1293, 0.2, e_PlayerRole_DM)
    builder.AddPlayer(0.2467, 0.344, e_PlayerRole_AM)
    builder.AddPlayer(0.2613, 0.1613, e_PlayerRole_CF)
    builder.AddPlayer(0.3533, 0.272, e_PlayerRole_AM)
