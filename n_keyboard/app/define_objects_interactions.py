from n_keyboard import constant as c
from n_keyboard.gui.components.keyboard_input_display import KeyboardInputDisplay
from n_keyboard.gui.state import State


def define_objects_interactions(input_display: KeyboardInputDisplay, state: State):
    state.attach(c.STATE, lambda value: input_display.label_state_display.configure(text=value))
    state.attach(c.CHAR, lambda value: input_display.label_char_display.configure(text=value))
    state.attach(c.KEYSYM, lambda value: input_display.label_keysysm_display.configure(text=value))
    state.attach(c.KEYSYM_NUM, lambda value: input_display.label_keysym_num_display.configure(text=value))
    state.attach(c.KEYCODE, lambda value: input_display.label_keycode_display.configure(text=value))
    state.attach(c.UNIQUE_KEY, lambda value: update_entry(input_display, value))
    input_display.attach_to_switch(lambda on_off: state.toggle_user_input_capture(on_off))


def update_entry(input_display: KeyboardInputDisplay, value):
    input_display.entry_unique_key.delete(0, 'end')
    input_display.entry_unique_key.insert(0, value)
