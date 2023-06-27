import tkinter as tk
from tkinter import ttk
from typing import Callable

from n_keyboard import constant as c
from n_keyboard.gui.bind_commands import upon_ok
from n_keyboard.gui.state import State
from .configuration_panel import ConfigurationPanel
from .keyboard_input_display import KeyboardInputDisplay


class Keyboard:
    def __init__(self, parent_frame: ttk.Frame):
        root = ttk.Frame(parent_frame, padding=(15, 15))
        root.grid(row=1, column=0, columnspan=2, sticky='nsew')

        label_style = "flat", "raised", "sunken", "ridge", "solid", "groove"

        row00 = '1234567890-='
        row01 = 'qwertyuiop[]'.upper()
        row02 = "asdfghjkl;'\\".upper()
        row03 = 'zxcvbnm,./'.upper()

        max_row = 0
        max_col = 0

        self._key_labels: dict[[str], ttk.Label] = dict()

        for r, row in enumerate((row00, row01, row02, row03)):
            max_row = max(max_row, r)
            for col, text in enumerate(list(row)):
                max_col = max(max_col, col)
                self.add_label_and_register(root, text, label_style, r + 1, col + 2)

        number_of_manual_rows = 2
        number_of_manual_columns = 2

        # Manual Keys
        # Row 0
        self.add_label_and_register(root, 'Escape', label_style, 0, 0, 2)
        for n in range(12):
            self.add_label_and_register(root, f'F{n + 1}', label_style, 0, n + number_of_manual_columns)

        # Row 1
        for n, text in enumerate(('Super_L', 'Control_L', 'Alt_L', 'Meta_L')):  # before space
            self.add_label_and_register(root, text, label_style, 5, n)

        self.add_label_and_register(root, 'Space', label_style, 5, 4, 5)  # exception / space

        for n, text in enumerate(('Meta_R', 'Alt_R', 'Left', 'Down', 'Up', 'Right')):  # after space
            self.add_label_and_register(root, text, label_style, 5, n + 9)

        # Left column
        self.add_label_and_register(root, '§', label_style, 1, 0, 2)
        self.add_label_and_register(root, 'Tab', label_style, 2, 0, 2)
        self.add_label_and_register(root, 'Caps_Lock', label_style, 3, 0, 2)
        self.add_label_and_register(root, 'Shift_L', label_style, 4, 0)
        self.add_label_and_register(root, '`', label_style, 4, 1)

        # Right column
        self.add_label_and_register(root, 'Backspace', label_style, 1, max_col + number_of_manual_columns + 1)
        self.add_label_and_register(root, 'Return', label_style, 2, max_col + number_of_manual_columns + 1, rowspan=2)
        self.add_label_and_register(root, 'Shift_R', label_style, 4, max_col + number_of_manual_columns - 1, 3)

        for row in range(max_row + number_of_manual_rows + 1):
            root.grid_rowconfigure(row, weight=1)
        for column in range(max_col + number_of_manual_columns + 2):
            root.grid_columnconfigure(column, weight=1)

    def add_label_and_register(self, root, text, label_style, row, column, columnspan=None, rowspan=None):
        label = ttk.Label(root, text=text, borderwidth=3, relief=label_style[1], anchor='center', width=25)
        label.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky='nswe')
        self._key_labels[text.lower()] = label

    def highlight_key(self, key: str):
        label = self._key_labels.get(key.lower())
        if label:
            label.configure(style=c.STYLE_LABEL_RED)

    def remove_highlight_key(self, key: str):
        label = self._key_labels.get(key.lower())
        if label:
            label.configure(style=c.STYLE_LABEL_DEFAULT)


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


def update_root_binding(root: tk.Tk, state: State, keyboard: Keyboard, input_display: KeyboardInputDisplay,
                        configuration_panel: ConfigurationPanel):
    # Bind root again

    def return_on_entry(e: tk.Event):
        if e.keysym.lower() == c.RETURN.lower():
            upon_ok(state, input_display)

    configuration_panel.entry_key.bind('<Key>', return_on_entry)
    root.bind('<Key>', lambda e: key_push(e, state, keyboard, input_display, configuration_panel))
    root.bind('<KeyRelease>', lambda e: key_release(e, state, keyboard))


def key_push(e: tk.Event, state: State, keyboard: Keyboard, input_display: KeyboardInputDisplay,
             configuration_panel: ConfigurationPanel):
    key = state.create_unique_key(e)
    rule = state.state
    if e.keysym.lower() == c.SPACE.lower():
        input_display.toggle_listen_to_user()
        state.toggle_user_input_capture(input_display.is_listening_to_user)

        entry_key = configuration_panel.entry_key
        entry_key.focus_set()
        entry_key.delete(0, tk.END)

    if rule_exists(key, rule):
        highlight_as_per_rule(key, rule, keyboard)
    else:
        keyboard.highlight_key(e.keysym)
        keyboard.highlight_key(e.char)
    state.set_text(e)


def key_release(e: tk.Event, state: State, keyboard: Keyboard):
    key = state.create_unique_key(e)
    rule = state.state
    if rule_exists(key, rule):
        remove_highlight_as_per_rule(key, rule, keyboard)
    else:
        keyboard.remove_highlight_key(e.keysym)
        keyboard.remove_highlight_key(e.char)
