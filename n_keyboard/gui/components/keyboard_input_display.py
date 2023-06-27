import tkinter as tk
from tkinter import ttk
from typing import Callable


class KeyboardInputDisplay:
    def __init__(self, parent_frame: ttk):
        root = ttk.Frame(parent_frame, padding=(15, 15))
        root.grid(row=0, column=0, sticky='nsew')
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(6, weight=1)
        root.grid_propagate(False)

        label_state = ttk.Label(root, text='state', width=25)
        label_char = ttk.Label(root, text='char', width=25)
        label_keysysm = ttk.Label(root, text='keysysm', width=25)
        label_keysym_num = ttk.Label(root, text='keysym_num', width=25)
        label_keycode = ttk.Label(root, text='keycode', width=25)

        self.label_state_display = ttk.Label(root)
        self.label_char_display = ttk.Label(root)
        self.label_keysysm_display = ttk.Label(root)
        self.label_keysym_num_display = ttk.Label(root)
        self.label_keycode_display = ttk.Label(root)

        self._var_combobox = tk.BooleanVar()
        self._var_combobox.set(True)
        label_capture_user_input = ttk.Label(root, width=25)
        check_button_capture_user_input = ttk.Checkbutton(root, variable=self._var_combobox, command=self.notify)

        label_state.grid(row=0, column=0, sticky='nsew')
        label_char.grid(row=1, column=0, sticky='nsew')
        label_keysysm.grid(row=2, column=0, sticky='nsew')
        label_keysym_num.grid(row=3, column=0, sticky='nsew')
        label_keycode.grid(row=4, column=0, sticky='nsew')

        self.label_state_display.grid(row=0, column=1, sticky='nsew')
        self.label_char_display.grid(row=1, column=1, sticky='nsew')
        self.label_keysysm_display.grid(row=2, column=1, sticky='nsew')
        self.label_keysym_num_display.grid(row=3, column=1, sticky='nsew')
        self.label_keycode_display.grid(row=4, column=1, sticky='nsew')

        label_capture_user_input.grid(row=5, column=0)
        check_button_capture_user_input.grid(row=5, column=1)

        self._subscribers = []

    def attach_to_switch(self, subscriber: Callable):
        self._subscribers.append(subscriber)

    def notify(self, *_):
        for subscriber in self._subscribers:
            subscriber(self._var_combobox.get())
