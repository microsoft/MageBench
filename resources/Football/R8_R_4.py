
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
    builder.SetBallPosition(-0.1973, 0.1827)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9533, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.2227, 0.0307, e_PlayerRole_CB)
    builder.AddPlayer(-0.2107, 0.1747, e_PlayerRole_RB)
    builder.AddPlayer(-0.1787, -0.1373, e_PlayerRole_CB)
    builder.AddPlayer(0.072, -0.3667, e_PlayerRole_LM)
    builder.AddPlayer(0.256, -0.248, e_PlayerRole_LM)
    builder.AddPlayer(0.26, 0.336, e_PlayerRole_RM)
    builder.AddPlayer(0.3053, -0.384, e_PlayerRole_LM)
    builder.AddPlayer(0.3707, 0.004, e_PlayerRole_CF)
    builder.AddPlayer(0.5733, -0.04, e_PlayerRole_CF)
    builder.AddPlayer(0.6493, 0.2333, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9747, -0.0053, e_PlayerRole_GK)
    builder.AddPlayer(-0.748, -0.168, e_PlayerRole_LB)
    builder.AddPlayer(-0.7027, 0.168, e_PlayerRole_RB)
    builder.AddPlayer(-0.6747, -0.04, e_PlayerRole_LB)
    builder.AddPlayer(-0.612, 0.3013, e_PlayerRole_RM)
    builder.AddPlayer(-0.4147, -0.0493, e_PlayerRole_LM)
    builder.AddPlayer(-0.3533, 0.224, e_PlayerRole_RM)
    builder.AddPlayer(-0.3307, 0.0573, e_PlayerRole_DM)
    builder.AddPlayer(-0.1893, 0.3107, e_PlayerRole_AM)
    builder.AddPlayer(-0.0253, 0.08, e_PlayerRole_CF)
    builder.AddPlayer(0.024, -0.0133, e_PlayerRole_CM)
