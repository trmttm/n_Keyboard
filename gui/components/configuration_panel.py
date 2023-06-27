import tkinter as tk
from tkinter import ttk


class ConfigurationPanel:
    def __init__(self, parent_frame: ttk.Frame, row=0, column=0, rowspan=None, columnspan=None):
        root = ttk.Frame(parent_frame, padding=(15, 15))
        root.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky='nsew')
        root.grid_columnconfigure(1, weight=1)
        root.grid_rowconfigure(15, weight=1)

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
