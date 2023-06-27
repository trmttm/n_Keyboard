from n_keyboard import constant as c
from n_keyboard.gui.components.keyboard_input_display import KeyboardInputDisplay
from n_keyboard.gui.state import State


def define_objects_interactions(input_display: KeyboardInputDisplay, state: State):
    state.attach(c.STATE, lambda value: input_display.label_state_display.configure(text=value))
    state.attach(c.CHAR, lambda value: input_display.label_state_display.configure(text=value))
    state.attach(c.KEYSYM, lambda value: input_display.label_state_display.configure(text=value))
    state.attach(c.KEYSYM_NUM, lambda value: input_display.label_state_display.configure(text=value))
    state.attach(c.KEYCODE, lambda value: input_display.label_state_display.configure(text=value))
    input_display.attach_to_switch(lambda on_off: state.toggle_user_input_capture(on_off))
