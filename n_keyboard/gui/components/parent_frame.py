from tkinter import Tk
from tkinter import ttk
from tkinter.ttk import Frame


def ParentFrame(root: Tk) -> Frame:
    frame_parent = ttk.Frame(root)
    frame_parent.grid_columnconfigure(0, weight=1)
    frame_parent.grid_columnconfigure(1, weight=1)
    frame_parent.grid_rowconfigure(0, weight=1)
    frame_parent.grid(row=0, column=0, sticky='nsew')
    frame_parent.grid_propagate(False)
    return frame_parent
