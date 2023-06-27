import tkinter as tk
from tkinter import ttk

from n_keyboard import constant as c


def instantiate_root() -> tk.Tk:
    root = tk.Tk()
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.grid_propagate(False)

    style = ttk.Style()
    themes = ('aqua', 'clam', 'alt', 'default', 'classic')
    style.theme_use(themes[2])
    style.configure(c.STYLE_LABEL_RED, foreground="red", background='yellow')

    return root
