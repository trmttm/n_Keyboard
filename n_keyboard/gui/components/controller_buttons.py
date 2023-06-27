from tkinter import ttk


class ControllerButtons:
    def __init__(self, parent_frame: ttk.Frame):
        frame_bottom = ttk.Frame(parent_frame)
        self.button_ok = ttk.Button(frame_bottom, text='OK')
        self.button_ok.grid(row=0, column=0)
        frame_bottom.grid(row=1, column=0, columnspan=2)
