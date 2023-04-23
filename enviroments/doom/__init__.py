import warnings

try:
    from rl_lab.enviroments.doom.vizdoom_basic_config import VizDoomBasicConfig
    from rl_lab.enviroments.doom.vizdoom_corridor_config import VizDoomCorridorConfig
    from rl_lab.enviroments.doom.vizdoom_deathmatch_config import VizDoomDeathmatchConfig
    from rl_lab.enviroments.doom.vizdoom_defend_center_config import VizDoomDefendCenterConfig
    from rl_lab.enviroments.doom.vizdoom_defend_line_config import VizDoomDefendLineConfig
    from rl_lab.enviroments.doom.vizdoom_health_gathering_config import \
        VizDoomHealthGatheringConfig
    from rl_lab.enviroments.doom.vizdoom_health_gathering_supreme import \
        VizDoomHealthGatheringSupremeConfig
    from rl_lab.enviroments.doom.vizdoom_my_way_home_config import VizDoomMyWayHomeConfig
    from rl_lab.enviroments.doom.vizdoom_predict_position_config import \
        VizDoomPredictPositionConfig
    from rl_lab.enviroments.doom.vizdoom_take_cover_config import VizDoomTakeCoverConfig

    AVAILABLE = True
except ImportError:
    warnings.warn('vizdoomgym not installed.')
    AVAILABLE = False
