import unittest


class MyTestCase(unittest.TestCase):
    def test_concept(self):
        import tkinter as tk
        from tkinter import ttk

        root = tk.Tk()
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)

        frame_display = ttk.Frame(root, padding=(15, 15))
        frame_display.grid(row=0, column=0, sticky='nsew')
        frame_display.grid_columnconfigure(0, weight=1)
        frame_display.grid_rowconfigure(6, weight=1)

        label_state = ttk.Label(frame_display, text='state', width=25)
        label_char = ttk.Label(frame_display, text='char', width=25)
        label_keysysm = ttk.Label(frame_display, text='keysysm', width=25)
        label_keysym_num = ttk.Label(frame_display, text='keysym_num', width=25)
        label_keycode = ttk.Label(frame_display, text='keycode', width=25)
        label_state.grid(row=0, column=0, sticky='nsew')
        label_char.grid(row=1, column=0, sticky='nsew')
        label_keysysm.grid(row=2, column=0, sticky='nsew')
        label_keysym_num.grid(row=3, column=0, sticky='nsew')
        label_keycode.grid(row=4, column=0, sticky='nsew')

        label_state_display = ttk.Label(frame_display)
        label_char_display = ttk.Label(frame_display)
        label_keysysm_display = ttk.Label(frame_display)
        label_keysym_num_display = ttk.Label(frame_display)
        label_keycode_display = ttk.Label(frame_display)
        label_state_display.grid(row=0, column=1, sticky='nsew')
        label_char_display.grid(row=1, column=1, sticky='nsew')
        label_keysysm_display.grid(row=2, column=1, sticky='nsew')
        label_keysym_num_display.grid(row=3, column=1, sticky='nsew')
        label_keycode_display.grid(row=4, column=1, sticky='nsew')

        var_capture_user_input = tk.BooleanVar()
        var_capture_user_input.set(True)
        label_capture_user_input = ttk.Label(frame_display, width=25)
        check_button_capture_user_input = ttk.Checkbutton(frame_display, variable=var_capture_user_input)

        label_capture_user_input.grid(row=5, column=0)
        check_button_capture_user_input.grid(row=5, column=1)

        state = dict()

        def update_state_upon_user_input(e: tk.Event):
            user_input = {
                'state': e.state,
                'char': e.char,
                'keysym': e.keysym,
                'keysym_num': e.keysym_num,
                'keycode': e.keycode,
            }
            new_state = {
                'user_input': user_input,
            }
            state.update(new_state)

        def update_state_upon_configuration():
            map_to = dict(zip(modifiers, tuple(var.get() for var in vars.values())))
            map_to.update({'key': entry_key.get()})
            new_state = {
                'map_to': map_to,
            }
            state.update(new_state)

        def set_text(e: tk.Event):
            if var_capture_user_input.get():
                label_state_display.configure(text=e.state)
                label_char_display.configure(text=e.char)
                label_keysysm_display.configure(text=e.keysym)
                label_keysym_num_display.configure(text=e.keysym_num)
                label_keycode_display.configure(text=e.keycode)
                update_state_upon_user_input(e)

        frame_configuration = ttk.Frame(root, padding=(15, 15))
        frame_configuration.grid(row=1, column=0, sticky='nsew')
        frame_configuration.grid_columnconfigure(1, weight=1)
        frame_configuration.grid_rowconfigure(5, weight=1)

        modifiers = ('Shift', 'Control', 'Command', 'Function')
        vars = dict(zip(modifiers, tuple(tk.BooleanVar() for _ in modifiers)))
        widgets = {}

        for n, modifier in enumerate(modifiers):
            label = ttk.Label(frame_configuration, text=modifier, width=25)
            check_button = ttk.Checkbutton(frame_configuration, variable=vars[modifier],
                                           command=update_state_upon_configuration)

            label.grid(row=n, column=0)
            check_button.grid(row=n, column=1)

            widgets[f'label_{modifier}'] = label
            widgets[f'check_button_{modifier}'] = check_button

        label_key = ttk.Label(frame_configuration, text='Key', width=25)
        entry_key = ttk.Entry(frame_configuration)
        entry_key.delete(0, tk.END)
        entry_key.insert(0, '')
        entry_key.bind('<KeyRelease>', lambda *_: update_state_upon_configuration())

        label_key.grid(row=len(modifiers), column=0)
        entry_key.grid(row=len(modifiers), column=1)

        frame_bottom = ttk.Frame(root)

        def upon_ok():
            import json
            path = 'shortcut.json'
            with open(path, 'w') as json_file:
                json.dump(state, json_file)
                print(f'Saved file to {path}.')

        button_ok = ttk.Button(frame_bottom, text='OK', command=upon_ok)
        button_ok.grid(row=0, column=0)
        frame_bottom.grid(row=2, column=0)

        root.bind('<Key>', set_text)
        root.mainloop()


if __name__ == '__main__':
    unittest.main()