
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
    builder.SetBallPosition(0.6693, 0.1253)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9747, 0.004, e_PlayerRole_GK)
    builder.AddPlayer(0.2307, 0.204, e_PlayerRole_RB)
    builder.AddPlayer(0.26, 0.0227, e_PlayerRole_CB)
    builder.AddPlayer(0.332, -0.22, e_PlayerRole_LB)
    builder.AddPlayer(0.4227, 0.116, e_PlayerRole_DM)
    builder.AddPlayer(0.492, -0.1507, e_PlayerRole_LM)
    builder.AddPlayer(0.524, 0.3427, e_PlayerRole_RM)
    builder.AddPlayer(0.66, 0.1307, e_PlayerRole_DM)
    builder.AddPlayer(0.7093, -0.28, e_PlayerRole_CM)
    builder.AddPlayer(0.8613, -0.1427, e_PlayerRole_CM)
    builder.AddPlayer(0.9333, 0.12, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9547, 0.0067, e_PlayerRole_GK)
    builder.AddPlayer(-0.8827, 0.308, e_PlayerRole_RB)
    builder.AddPlayer(-0.88, -0.3147, e_PlayerRole_LB)
    builder.AddPlayer(-0.8453, -0.0307, e_PlayerRole_CB)
    builder.AddPlayer(-0.676, 0.312, e_PlayerRole_RM)
    builder.AddPlayer(-0.6293, 0.0173, e_PlayerRole_DM)
    builder.AddPlayer(-0.4507, -0.288, e_PlayerRole_LM)
    builder.AddPlayer(-0.448, 0.348, e_PlayerRole_RM)
    builder.AddPlayer(-0.392, 0.192, e_PlayerRole_AM)
    builder.AddPlayer(-0.3893, -0.08, e_PlayerRole_CF)
    builder.AddPlayer(-0.3133, 0.0067, e_PlayerRole_CF)
