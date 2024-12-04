
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
    builder.SetBallPosition(-0.8587, 0.2387)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9747, -0.012, e_PlayerRole_GK)
    builder.AddPlayer(-0.8707, 0.2333, e_PlayerRole_RB)
    builder.AddPlayer(-0.7027, 0.1507, e_PlayerRole_CB)
    builder.AddPlayer(-0.644, -0.052, e_PlayerRole_LB)
    builder.AddPlayer(-0.628, 0.372, e_PlayerRole_RM)
    builder.AddPlayer(-0.4373, 0.084, e_PlayerRole_DM)
    builder.AddPlayer(-0.3693, 0.2827, e_PlayerRole_RM)
    builder.AddPlayer(-0.3347, -0.248, e_PlayerRole_LM)
    builder.AddPlayer(-0.1507, 0.3587, e_PlayerRole_AM)
    builder.AddPlayer(-0.088, 0.212, e_PlayerRole_AM)
    builder.AddPlayer(0.1133, -0.0387, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.98, -0.0187, e_PlayerRole_GK)
    builder.AddPlayer(-0.2587, -0.184, e_PlayerRole_LB)
    builder.AddPlayer(-0.1707, 0.036, e_PlayerRole_RB)
    builder.AddPlayer(0.012, -0.2507, e_PlayerRole_LB)
    builder.AddPlayer(0.0507, -0.3587, e_PlayerRole_LM)
    builder.AddPlayer(0.172, 0.132, e_PlayerRole_RM)
    builder.AddPlayer(0.288, -0.1787, e_PlayerRole_LM)
    builder.AddPlayer(0.3653, 0.2053, e_PlayerRole_RM)
    builder.AddPlayer(0.5053, -0.2253, e_PlayerRole_CM)
    builder.AddPlayer(0.5453, -0.1093, e_PlayerRole_CF)
    builder.AddPlayer(0.7307, -0.2493, e_PlayerRole_CM)
