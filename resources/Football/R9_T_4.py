
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
    builder.SetBallPosition(0.9773, 0.3027)

    builder.SetTeam(Team.e_Left)

    builder.AddPlayer(-0.9547, -0.0067, e_PlayerRole_GK)
    builder.AddPlayer(0.1267, 0.1307, e_PlayerRole_CB)
    builder.AddPlayer(0.3387, -0.0307, e_PlayerRole_CB)
    builder.AddPlayer(0.388, 0.2173, e_PlayerRole_RB)
    builder.AddPlayer(0.488, -0.1667, e_PlayerRole_LM)
    builder.AddPlayer(0.6347, 0.3907, e_PlayerRole_RM)
    builder.AddPlayer(0.6653, 0.0373, e_PlayerRole_DM)
    builder.AddPlayer(0.7693, -0.2933, e_PlayerRole_LM)
    builder.AddPlayer(0.8213, -0.1373, e_PlayerRole_CM)
    builder.AddPlayer(0.8627, 0.0373, e_PlayerRole_CF)
    builder.AddPlayer(0.9853, 0.304, e_PlayerRole_AM)


    builder.SetTeam(Team.e_Right)

    builder.AddPlayer(-0.9707, -0.0293, e_PlayerRole_GK)
    builder.AddPlayer(-0.9227, -0.3667, e_PlayerRole_LB)
    builder.AddPlayer(-0.8387, -0.1453, e_PlayerRole_CB)
    builder.AddPlayer(-0.796, 0.0893, e_PlayerRole_RB)
    builder.AddPlayer(-0.6987, 0.2493, e_PlayerRole_RM)
    builder.AddPlayer(-0.6973, 0.104, e_PlayerRole_RM)
    builder.AddPlayer(-0.6107, -0.084, e_PlayerRole_DM)
    builder.AddPlayer(-0.5787, -0.248, e_PlayerRole_LM)
    builder.AddPlayer(-0.5373, 0.0907, e_PlayerRole_AM)
    builder.AddPlayer(-0.52, -0.3707, e_PlayerRole_CM)
    builder.AddPlayer(-0.244, -0.1533, e_PlayerRole_CF)
