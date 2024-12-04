
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
    builder.SetBallPosition(0.1093, -0.0627)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9533, -0.0107, e_PlayerRole_GK)
    builder.AddPlayer(-0.024, 0.1733, e_PlayerRole_RB)
    builder.AddPlayer(0.0187, -0.1507, e_PlayerRole_CB)
    builder.AddPlayer(0.1013, -0.0653, e_PlayerRole_CB)
    builder.AddPlayer(0.176, -0.34, e_PlayerRole_LM)
    builder.AddPlayer(0.4293, -0.364, e_PlayerRole_LM)
    builder.AddPlayer(0.4893, -0.076, e_PlayerRole_DM)
    builder.AddPlayer(0.5707, -0.3987, e_PlayerRole_LM)
    builder.AddPlayer(0.664, -0.2693, e_PlayerRole_CM)
    builder.AddPlayer(0.6853, 0.328, e_PlayerRole_AM)
    builder.AddPlayer(0.7787, 0.0133, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9653, -0.0067, e_PlayerRole_GK)
    builder.AddPlayer(-0.8027, -0.1707, e_PlayerRole_LB)
    builder.AddPlayer(-0.7533, 0.04, e_PlayerRole_CB)
    builder.AddPlayer(-0.74, 0.1627, e_PlayerRole_CB)
    builder.AddPlayer(-0.696, 0.2907, e_PlayerRole_RM)
    builder.AddPlayer(-0.548, -0.0453, e_PlayerRole_LM)
    builder.AddPlayer(-0.532, 0.348, e_PlayerRole_RM)
    builder.AddPlayer(-0.5267, 0.1573, e_PlayerRole_DM)
    builder.AddPlayer(-0.2587, -0.0627, e_PlayerRole_CM)
    builder.AddPlayer(-0.2587, 0.2893, e_PlayerRole_AM)
    builder.AddPlayer(-0.1867, 0.0827, e_PlayerRole_CF)
