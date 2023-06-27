from typing import Callable

from n_keyboard import constant as c
from n_keyboard.gui.bind_commands import bind_commands
from n_keyboard.gui.components.configuration_panel import ConfigurationPanel
from n_keyboard.gui.components.controller_buttons import ControllerButtons
from n_keyboard.gui.components.keyboard import Keyboard
from n_keyboard.gui.components.keyboard_input_display import KeyboardInputDisplay
from n_keyboard.gui.components.parent_frame import ParentFrame
from n_keyboard.gui.components.root import instantiate_root
from .define_objects_interactions import define_objects_interactions
from .gui_state import instantiate_state


def rule_exists(key: str, rule: dict) -> bool:
    return key in rule and rule.get(key).get(c.USER_INPUT)


def highlight_as_per_rule(unique_key: str, rule: dict, keyboard: Keyboard):
    user_input = rule.get(unique_key).get(c.USER_INPUT)
    key = user_input.get(c.KEY)
    set_or_remove_highlight(key, user_input, keyboard.highlight_key)


def remove_highlight_as_per_rule(unique_key: str, rule: dict, keyboard: Keyboard):
    user_input = rule.get(unique_key).get(c.USER_INPUT)
    key = user_input.get(c.KEY)
    set_or_remove_highlight(key, user_input, keyboard.remove_highlight_key)


def set_or_remove_highlight(key: str, user_input: dict, set_or_remove_highlight: Callable):
    set_or_remove_highlight(key)
    if user_input.get(c.SHIFT):
        set_or_remove_highlight(c.SHIFT_L)
    if user_input.get(c.CONTROL):
        set_or_remove_highlight(c.CONTROL_L)
    if user_input.get(c.COMMAND):
        set_or_remove_highlight(c.COMMAND_L)
    if user_input.get(c.OPTION):
        set_or_remove_highlight(c.OPTION_L)
    if user_input.get(c.ALT):
        set_or_remove_highlight(c.ALT_L)
    if user_input.get(c.FUNCTION):
        set_or_remove_highlight(c.FUNCTION_L)


class App:
    def __init__(self, root=None, width=800, height=400):
        if root is None:  # root may be toplevel, passed by client application.
            root = instantiate_root(width, height)
        self._root = root

        self._load_gui()
        self._instantiate_state()
        self._define_objects_interactions()
        self._fix_frame()
        self._bind_commands()

    def _load_gui(self):
        # Each GUI components positions are hardcoded in their constructor.
        self._parent_frame = parent_frame = ParentFrame(self._root).frame
        self._input_display = KeyboardInputDisplay(parent_frame)
        self._configuration_panel = ConfigurationPanel(parent_frame)
        self._controller_buttons = ControllerButtons(parent_frame)

    def _instantiate_state(self):
        self._state = instantiate_state(self._configuration_panel)

    def _define_objects_interactions(self):
        define_objects_interactions(self._input_display, self._state)

    def _bind_commands(self):
        bind_commands(self._configuration_panel, self._controller_buttons, self._root, self._state)

    def display_keyboard(self):
        keyboard = Keyboard(self._parent_frame)

        # re-configure row and re-position controller buttons
        self._parent_frame.grid_rowconfigure(1, weight=1)
        self._controller_buttons.grid(row=2, column=0, columnspan=2)

        # Bind root again
        import tkinter as tk

        def key_push(e: tk.Event):
            # rule 01 if json specifies, then follow that rule.
            key = self._state.create_unique_key(e)
            rule = self._state.state
            if rule_exists(key, rule):
                highlight_as_per_rule(key, rule, keyboard)
            else:
                keyboard.highlight_key(e.keysym)
                keyboard.highlight_key(e.char)
            self._state.set_text(e)

        def key_release(e: tk.Event):
            key = self._state.create_unique_key(e)
            rule = self._state.state
            if rule_exists(key, rule):
                remove_highlight_as_per_rule(key, rule, keyboard)
            else:
                keyboard.remove_highlight_key(e.keysym)
                keyboard.remove_highlight_key(e.char)

        self._root.bind('<Key>', key_push)
        self._root.bind('<KeyRelease>', key_release)

    def _fix_frame(self):
        self._configuration_panel.fix_frame_size()
        self._input_display.fix_frame_size()

    def run(self):
        self._root.mainloop()
