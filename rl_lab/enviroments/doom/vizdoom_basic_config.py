from rl_lab.enviroments.doom.doom_default_config import DoomDefaultConfig


class VizDoomBasicConfig(DoomDefaultConfig):
    """Defines specific config for this env."""
    env_spec = 'VizdoomBasic-v0'
    n_actions = 3
