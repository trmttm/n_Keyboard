import tkinter as tk
from tkinter import ttk

from n_keyboard import constant as c


def instantiate_root(width=800, height=400) -> tk.Tk:
    root = tk.Tk()
    root.geometry(f'{width}x{height}')
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    style = ttk.Style()
    themes = ('aqua', 'clam', 'alt', 'default', 'classic')
    style.theme_use(themes[3])
    style.configure(c.STYLE_LABEL_RED, foreground="red", background='yellow')

    return root
