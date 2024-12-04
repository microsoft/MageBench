
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
    builder.SetBallPosition(0.8387, -0.336)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.944, -0.0013, e_PlayerRole_GK)
    builder.AddPlayer(0.424, -0.3333, e_PlayerRole_LB)
    builder.AddPlayer(0.5293, 0.2107, e_PlayerRole_RB)
    builder.AddPlayer(0.6013, -0.1653, e_PlayerRole_LB)
    builder.AddPlayer(0.6853, -0.256, e_PlayerRole_LM)
    builder.AddPlayer(0.6853, 0.0227, e_PlayerRole_DM)
    builder.AddPlayer(0.7773, 0.064, e_PlayerRole_RM)
    builder.AddPlayer(0.788, -0.1907, e_PlayerRole_LM)
    builder.AddPlayer(0.8053, -0.0307, e_PlayerRole_CF)
    builder.AddPlayer(0.836, 0.112, e_PlayerRole_AM)
    builder.AddPlayer(0.8373, -0.344, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.956, 0.0547, e_PlayerRole_GK)
    builder.AddPlayer(-0.9107, 0.228, e_PlayerRole_RB)
    builder.AddPlayer(-0.8493, -0.0653, e_PlayerRole_CB)
    builder.AddPlayer(-0.8453, -0.1627, e_PlayerRole_LB)
    builder.AddPlayer(-0.844, 0.1733, e_PlayerRole_RM)
    builder.AddPlayer(-0.84, -0.328, e_PlayerRole_LM)
    builder.AddPlayer(-0.8333, 0.0053, e_PlayerRole_DM)
    builder.AddPlayer(-0.8147, 0.06, e_PlayerRole_RM)
    builder.AddPlayer(-0.7507, 0.1133, e_PlayerRole_AM)
    builder.AddPlayer(-0.744, -0.0413, e_PlayerRole_CF)
    builder.AddPlayer(-0.6973, -0.2173, e_PlayerRole_CM)
