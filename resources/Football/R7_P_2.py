
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
    builder.SetBallPosition(-0.7827, 0.3773)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.988, -0.0013, e_PlayerRole_GK)
    builder.AddPlayer(-0.8987, 0.26, e_PlayerRole_RB)
    builder.AddPlayer(-0.796, 0.3747, e_PlayerRole_RB)
    builder.AddPlayer(-0.6893, 0.0853, e_PlayerRole_CB)
    builder.AddPlayer(-0.6387, -0.16, e_PlayerRole_LM)
    builder.AddPlayer(-0.516, 0.248, e_PlayerRole_RM)
    builder.AddPlayer(-0.2853, -0.184, e_PlayerRole_LM)
    builder.AddPlayer(-0.1533, 0.02, e_PlayerRole_DM)
    builder.AddPlayer(0.0507, -0.2027, e_PlayerRole_CM)
    builder.AddPlayer(0.1627, -0.032, e_PlayerRole_CM)
    builder.AddPlayer(0.3427, -0.1947, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9253, -0.0347, e_PlayerRole_GK)
    builder.AddPlayer(-0.38, -0.068, e_PlayerRole_CB)
    builder.AddPlayer(0.0493, 0.112, e_PlayerRole_RB)
    builder.AddPlayer(0.0587, -0.0613, e_PlayerRole_CB)
    builder.AddPlayer(0.2893, -0.2507, e_PlayerRole_LM)
    builder.AddPlayer(0.3333, -0.0573, e_PlayerRole_DM)
    builder.AddPlayer(0.5507, -0.2787, e_PlayerRole_LM)
    builder.AddPlayer(0.684, -0.132, e_PlayerRole_DM)
    builder.AddPlayer(0.8493, -0.324, e_PlayerRole_CM)
    builder.AddPlayer(0.8707, -0.04, e_PlayerRole_CF)
    builder.AddPlayer(0.9453, -0.292, e_PlayerRole_CM)
