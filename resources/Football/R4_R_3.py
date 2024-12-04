
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
    builder.SetBallPosition(-0.96, -0.0053)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.968, -0.008, e_PlayerRole_GK)
    builder.AddPlayer(-0.8653, 0.208, e_PlayerRole_RB)
    builder.AddPlayer(-0.804, -0.0467, e_PlayerRole_CB)
    builder.AddPlayer(-0.7493, 0.0547, e_PlayerRole_RB)
    builder.AddPlayer(-0.6413, -0.3147, e_PlayerRole_LM)
    builder.AddPlayer(-0.4507, -0.0827, e_PlayerRole_DM)
    builder.AddPlayer(-0.1133, -0.38, e_PlayerRole_LM)
    builder.AddPlayer(0.072, 0.2227, e_PlayerRole_RM)
    builder.AddPlayer(0.0987, 0.0027, e_PlayerRole_CF)
    builder.AddPlayer(0.1587, -0.3413, e_PlayerRole_CM)
    builder.AddPlayer(0.2547, -0.1587, e_PlayerRole_CF)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9587, -0.0067, e_PlayerRole_GK)
    builder.AddPlayer(-0.3387, 0.0747, e_PlayerRole_CB)
    builder.AddPlayer(0.036, 0.3453, e_PlayerRole_RB)
    builder.AddPlayer(0.0547, 0.2053, e_PlayerRole_RB)
    builder.AddPlayer(0.1867, -0.1173, e_PlayerRole_LM)
    builder.AddPlayer(0.2507, 0.2093, e_PlayerRole_RM)
    builder.AddPlayer(0.2547, 0.36, e_PlayerRole_RM)
    builder.AddPlayer(0.5333, 0.368, e_PlayerRole_RM)
    builder.AddPlayer(0.616, -0.1747, e_PlayerRole_CM)
    builder.AddPlayer(0.696, 0.1307, e_PlayerRole_CF)
    builder.AddPlayer(0.704, -0.0573, e_PlayerRole_CM)
