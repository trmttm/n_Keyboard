from tkinter import ttk

from n_keyboard import constant as c


class Keyboard:
    def __init__(self, parent_frame: ttk.Frame):
        root = ttk.Frame(parent_frame, padding=(15, 15))
        root.grid(row=1, column=0, columnspan=2, sticky='nsew')

        row00 = '1234567890-='
        row01 = 'qwertyuiop[]'.upper()
        row02 = "asdfghjkl;'\\".upper()
        row03 = 'zxcvbnm,./'.upper()

        max_row = 0
        max_col = 0

        self._key_labels: dict[[str], ttk.Label] = dict()

        label_style = "flat", "raised", "sunken", "ridge", "solid", "groove"
        for r, row in enumerate((row00, row01, row02, row03)):
            max_row = max(max_row, r)
            for col, text in enumerate(list(row)):
                max_col = max(max_col, col)
                label = ttk.Label(root, text=text, borderwidth=3, relief=label_style[1], anchor='center')
                label.grid(row=r + 1, column=col + 2, sticky='nswe')
                self._key_labels[text.lower()] = label

        number_of_manual_rows = 2
        number_of_manual_columns = 2

        # Manual Keys
        # Row 0
        label = ttk.Label(root, text='Escape', borderwidth=3, relief=label_style[1], anchor='center')
        label.grid(row=0, column=0, columnspan=2, sticky='nswe')
        for n in range(12):
            label = ttk.Label(root, text=f'F{n + 1}', borderwidth=3, relief=label_style[1], anchor='center', width=25)
            label.grid(row=0, column=n + number_of_manual_columns, sticky='nswe')

        # Row 1
        for n, text in enumerate(('fn', 'control', 'option', 'command')):
            label = ttk.Label(root, text=text, borderwidth=3, relief=label_style[1], anchor='center', width=25)
            label.grid(row=5, column=n, sticky='nswe')
        label = ttk.Label(root, text='Space', borderwidth=3, relief=label_style[1], anchor='center', width=25)
        label.grid(row=5, column=4, columnspan=5, sticky='nswe')
        label = ttk.Label(root, text='command', borderwidth=3, relief=label_style[1], anchor='center', width=25)
        label.grid(row=5, column=9, sticky='nswe')
        label = ttk.Label(root, text='option', borderwidth=3, relief=label_style[1], anchor='center', width=25)
        label.grid(row=5, column=10, sticky='nswe')
        label = ttk.Label(root, text='←', borderwidth=3, relief=label_style[1], anchor='center', width=25)
        label.grid(row=5, column=11, sticky='nswe')
        label = ttk.Label(root, text='↑', borderwidth=3, relief=label_style[1], anchor='center', width=25)
        label.grid(row=5, column=12, sticky='nswe')
        label = ttk.Label(root, text='↓', borderwidth=3, relief=label_style[1], anchor='center', width=25)
        label.grid(row=5, column=13, sticky='nswe')
        label = ttk.Label(root, text='→', borderwidth=3, relief=label_style[1], anchor='center', width=25)
        label.grid(row=5, column=14, sticky='nswe')

        # Left column
        label = ttk.Label(root, text='§', borderwidth=3, relief=label_style[1], anchor='center', width=25)
        label.grid(row=1, column=0, columnspan=2, sticky='nswe')
        label = ttk.Label(root, text='Tab', borderwidth=3, relief=label_style[1], anchor='center', width=25)
        label.grid(row=2, column=0, columnspan=2, sticky='nswe')
        label = ttk.Label(root, text='CapLock', borderwidth=3, relief=label_style[1], anchor='center', width=25)
        label.grid(row=3, column=0, columnspan=2, sticky='nswe')
        label = ttk.Label(root, text='Shift_L', borderwidth=3, relief=label_style[1], anchor='center', width=25)
        label.grid(row=4, column=0, sticky='nswe')
        label = ttk.Label(root, text='`', borderwidth=3, relief=label_style[1], anchor='center', width=25)
        label.grid(row=4, column=1, sticky='nswe')

        # Right column
        label = ttk.Label(root, text='Backspace', borderwidth=3, relief=label_style[1], anchor='center', width=25)
        label.grid(row=1, column=max_col + number_of_manual_columns + 1, sticky='nswe')
        label = ttk.Label(root, text='Return', borderwidth=3, relief=label_style[1], anchor='center', width=25)
        label.grid(row=2, column=max_col + number_of_manual_columns + 1, rowspan=2, sticky='nswe')
        label = ttk.Label(root, text='Shift_R', borderwidth=3, relief=label_style[1], anchor='center', width=25)
        label.grid(row=4, column=max_col + number_of_manual_columns - 1, columnspan=3, sticky='nswe')

        for row in range(max_row + number_of_manual_rows + 1):
            root.grid_rowconfigure(row, weight=1)
        for column in range(max_col + number_of_manual_columns + 2):
            root.grid_columnconfigure(column, weight=1)

    def highlight_key(self, key: str):
        label = self._key_labels.get(key.lower())
        if label:
            label.configure(style=c.STYLE_LABEL_RED)

    def remove_highlight_key(self, key: str):
        label = self._key_labels.get(key.lower())
        if label:
            label.configure(style=c.STYLE_LABEL_DEFAULT)
