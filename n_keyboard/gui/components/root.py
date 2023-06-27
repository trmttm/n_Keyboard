import tkinter as tk


def instantiate_root() -> tk.Tk:
    import tkinter as tk
    root = tk.Tk()
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    return root