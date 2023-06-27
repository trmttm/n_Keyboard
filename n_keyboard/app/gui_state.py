from n_keyboard import constant as c
from n_keyboard.gui.components.configuration_panel import ConfigurationPanel
from n_keyboard.gui.state import State


def instantiate_state(configuration_panel: ConfigurationPanel) -> State:
    state = State(configuration_panel.get_user_input, c.FILE_NAME)
    return state
