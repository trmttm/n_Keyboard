from tkinter import ttk


class ControllerButtons:
    def __init__(self, parent_frame: ttk.Frame):
        root = ttk.Frame(parent_frame, padding=(0, 15))
        self.button_ok = ttk.Button(root, text='OK')
        self.button_ok.grid(row=0, column=0)
        root.grid(row=1, column=0, columnspan=2)
        self._root = root

    def grid(self, *args, **kwargs):
        self._root.grid(*args, **kwargs)
