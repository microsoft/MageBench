
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
    builder.SetBallPosition(-0.0427, -0.0227)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9773, -0.0053, e_PlayerRole_GK)
    builder.AddPlayer(-0.8027, 0.1213, e_PlayerRole_RB)
    builder.AddPlayer(-0.78, -0.0293, e_PlayerRole_CB)
    builder.AddPlayer(-0.6093, -0.2387, e_PlayerRole_LB)
    builder.AddPlayer(-0.6013, 0.0293, e_PlayerRole_DM)
    builder.AddPlayer(-0.5707, -0.116, e_PlayerRole_LM)
    builder.AddPlayer(-0.5053, 0.032, e_PlayerRole_DM)
    builder.AddPlayer(-0.4787, -0.092, e_PlayerRole_DM)
    builder.AddPlayer(-0.4747, 0.1987, e_PlayerRole_AM)
    builder.AddPlayer(-0.324, -0.1947, e_PlayerRole_CM)
    builder.AddPlayer(-0.06, -0.0213, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.98, -0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.688, -0.1933, e_PlayerRole_LB)
    builder.AddPlayer(-0.6693, 0.2787, e_PlayerRole_RB)
    builder.AddPlayer(-0.0773, 0.0653, e_PlayerRole_CB)
    builder.AddPlayer(0.2733, 0.2027, e_PlayerRole_RM)
    builder.AddPlayer(0.4293, -0.1747, e_PlayerRole_LM)
    builder.AddPlayer(0.4373, 0.0893, e_PlayerRole_DM)
    builder.AddPlayer(0.4627, -0.0267, e_PlayerRole_DM)
    builder.AddPlayer(0.5787, 0.2293, e_PlayerRole_AM)
    builder.AddPlayer(0.7547, 0.028, e_PlayerRole_CF)
    builder.AddPlayer(0.7627, -0.112, e_PlayerRole_CM)
