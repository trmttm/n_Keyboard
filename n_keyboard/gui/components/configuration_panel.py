import tkinter as tk
from tkinter import ttk

from n_keyboard import constant as c


class ConfigurationPanel:
    def __init__(self, parent_frame: ttk.Frame):
        root = ttk.Frame(parent_frame, padding=(15, 15))
        root.grid(row=0, column=1, sticky='nsew')
        root.grid_columnconfigure(1, weight=1)
        root.grid_rowconfigure(15, weight=1)
        root.grid_propagate(False)

        self.modifiers = ('Shift', 'Control', 'Command', 'Option', 'Alt', 'Function')
        self.vars = dict(zip(self.modifiers, tuple(tk.BooleanVar() for _ in self.modifiers)))
        self.check_buttons = []

        for n, modifier in enumerate(self.modifiers):
            label = ttk.Label(root, text=modifier, width=25)
            check_button = ttk.Checkbutton(root, variable=self.vars[modifier])
            self.check_buttons.append(check_button)

            label.grid(row=n, column=0)
            check_button.grid(row=n, column=1)

        label_key = ttk.Label(root, text='Key', width=25)
        self.entry_key = ttk.Entry(root)

        label_key.grid(row=len(self.modifiers), column=0)
        self.entry_key.grid(row=len(self.modifiers), column=1)

    def get_user_input(self) -> dict:
        user_input = dict(zip(self.modifiers, tuple(var.get() for var in self.vars.values())))
        user_input.update({c.KEY: self.entry_key.get()})
        return user_input
