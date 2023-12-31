from tkinter import Tk

from n_keyboard.gui.components.configuration_panel import ConfigurationPanel
from n_keyboard.gui.components.controller_buttons import ControllerButtons
from n_keyboard.gui.components.keyboard_input_display import KeyboardInputDisplay
from n_keyboard.gui.state import State


def bind_commands(config_panel: ConfigurationPanel, controller_buttons: ControllerButtons,
                  input_display: KeyboardInputDisplay, root: Tk, state: State):
    root.bind('<Key>', state.set_text)

    controller_buttons.button_ok['command'] = lambda: upon_ok(state, input_display)
    for check_button in config_panel.check_buttons:
        check_button['command'] = lambda *_: state.update_state_upon_configuration()
    config_panel.entry_key.bind('<KeyRelease>', lambda *_: state.update_state_upon_configuration())


def upon_ok(state: State, input_display: KeyboardInputDisplay):
    state.upon_ok()
    input_display.set_listen_to_user_on()
    state.toggle_user_input_capture(True)
