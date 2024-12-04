
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
    builder.SetBallPosition(-0.068, 0.304)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9773, 0.0027, e_PlayerRole_GK)
    builder.AddPlayer(-0.656, 0.2253, e_PlayerRole_CB)
    builder.AddPlayer(-0.472, -0.0827, e_PlayerRole_LB)
    builder.AddPlayer(-0.3813, 0.0547, e_PlayerRole_CB)
    builder.AddPlayer(-0.332, 0.3533, e_PlayerRole_RM)
    builder.AddPlayer(-0.212, -0.08, e_PlayerRole_LM)
    builder.AddPlayer(-0.1187, 0.144, e_PlayerRole_DM)
    builder.AddPlayer(-0.0787, 0.304, e_PlayerRole_RM)
    builder.AddPlayer(0.076, -0.0333, e_PlayerRole_CM)
    builder.AddPlayer(0.0813, 0.3973, e_PlayerRole_AM)
    builder.AddPlayer(0.3627, -0.1187, e_PlayerRole_CM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9467, -0.012, e_PlayerRole_GK)
    builder.AddPlayer(-0.5013, 0.2293, e_PlayerRole_RB)
    builder.AddPlayer(-0.2187, -0.0653, e_PlayerRole_CB)
    builder.AddPlayer(-0.1427, 0.084, e_PlayerRole_RB)
    builder.AddPlayer(-0.056, -0.3, e_PlayerRole_LM)
    builder.AddPlayer(0.0667, -0.1227, e_PlayerRole_DM)
    builder.AddPlayer(0.1653, 0.0653, e_PlayerRole_RM)
    builder.AddPlayer(0.288, -0.3533, e_PlayerRole_LM)
    builder.AddPlayer(0.308, -0.0427, e_PlayerRole_CF)
    builder.AddPlayer(0.564, 0.1667, e_PlayerRole_AM)
    builder.AddPlayer(0.6973, -0.1827, e_PlayerRole_CM)
