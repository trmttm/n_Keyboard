from tkinter import ttk

from n_keyboard import constant as c


class Keyboard:
    def __init__(self, parent_frame: ttk.Frame):
        root = ttk.Frame(parent_frame, padding=(15, 15))
        root.grid(row=1, column=0, columnspan=2, sticky='nsew')

        row00 = '1234567890-='
        row01 = 'qwertyuiop[]'.upper()
        row02 = 'asdfghjkl;\\'.upper()
        row03 = '`zxcvbnm,./'.upper()

        max_row = 0
        max_col = 0

        self._key_labels: dict[[str], ttk.Label] = dict()

        label_style = "flat", "raised", "sunken", "ridge", "solid", "groove"
        for r, row in enumerate((row00, row01, row02, row03)):
            max_row = max(max_row, r)
            for c, text in enumerate(list(row)):
                max_col = max(max_col, c)
                label = ttk.Label(root, text=text, borderwidth=3, relief=label_style[1], anchor='center')
                label.grid(row=r, column=c, sticky='nswe')
                self._key_labels[text.lower()] = label

        for row in range(max_row):
            root.grid_rowconfigure(row, weight=1)
        for column in range(max_col + 1):
            root.grid_columnconfigure(column, weight=1)

    def highlight_key(self, key: str):
        label = self._key_labels.get(key.lower())
        if label:
            label.configure(style=c.STYLE_LABEL_RED)

    def remove_highlight_key(self, key: str):
        label = self._key_labels.get(key.lower())
        if label:
            label.configure(style=c.STYLE_LABEL_DEFAULT)
