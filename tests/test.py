import unittest


class MyTestCase(unittest.TestCase):
    def test_concept(self):
        import json
        path = 'shortcut.json'
        with open(path, 'r') as json_file:
            try:
                state = json.load(json_file)
            except:
                state = dict()

        def upon_ok():
            clean_state = {}
            for keycode, data in state.items():
                if 'user_input' in data:
                    clean_state[keycode] = data
            with open(path, 'w') as json_file:
                json.dump(clean_state, json_file)
                print(f'Saved file to {path}.')

        keycode = None

        import tkinter as tk
        from tkinter import ttk

        root = tk.Tk()
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)

        frame_row_01 = ttk.Frame(root)
        frame_row_01.grid_columnconfigure(0, weight=1)
        frame_row_01.grid_columnconfigure(1, weight=1)
        frame_row_01.grid_rowconfigure(0, weight=1)
        frame_row_01.grid(row=0, column=0, sticky='nsew')

        frame_display = ttk.Frame(frame_row_01, padding=(15, 15))
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

        def update_state_upon_user_input(e: tk.Event):
            nonlocal keycode
            keycode = e.keycode
            new_state = {
                e.keycode: {'system_state': {
                    'state': e.state,
                    'char': e.char,
                    'keysym': e.keysym,
                    'keysym_num': e.keysym_num,
                }}
            }
            state.update(new_state)

        def update_state_upon_configuration():
            system_state = state.get(keycode)
            if system_state:
                user_input = dict(zip(modifiers, tuple(var.get() for var in vars.values())))
                user_input.update({'key': entry_key.get()})
                system_state.update({'user_input': user_input})
                new_state = {
                    keycode: system_state,
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

        frame_configuration = ttk.Frame(frame_row_01, padding=(15, 15))
        frame_configuration.grid(row=0, column=1, sticky='nsew')
        frame_configuration.grid_columnconfigure(1, weight=1)
        frame_configuration.grid_rowconfigure(15, weight=1)

        modifiers = ('Shift', 'Control', 'Command', 'Option', 'Alt', 'Function')
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

        button_ok = ttk.Button(frame_bottom, text='OK', command=upon_ok)
        button_ok.grid(row=0, column=0)
        frame_bottom.grid(row=1, column=0)

        root.bind('<Key>', set_text)
        root.mainloop()

    def test_oop_refactoring(self):
        from n_keyboard.gui.components.root import instantiate_root
        from n_keyboard import constant as c
        from n_keyboard.gui.components.keyboard_input_display import KeyboardInputDisplay
        from n_keyboard.gui.components.configuration_panel import ConfigurationPanel
        from n_keyboard.gui.components.controller_buttons import ControllerButtons

        root = instantiate_root()

        from tkinter import ttk
        frame_parent = ttk.Frame(root)
        frame_parent.grid_columnconfigure(0, weight=1)
        frame_parent.grid_columnconfigure(1, weight=1)
        frame_parent.grid_rowconfigure(0, weight=1)
        frame_parent.grid(row=0, column=0, sticky='nsew')

        input_display = KeyboardInputDisplay(frame_parent)
        configuration_panel = ConfigurationPanel(frame_parent)
        controller_buttons = ControllerButtons(frame_parent)

        from n_keyboard.gui.state import State
        state = State(configuration_panel.get_user_input, 'shortcut.json')

        # Define interactions between objects
        state.attach(c.STATE, lambda value: input_display.label_state_display.configure(text=value))
        state.attach(c.CHAR, lambda value: input_display.label_char_display.configure(text=value))
        state.attach(c.KEYSYM, lambda value: input_display.label_keysysm_display.configure(text=value))
        state.attach(c.KEYSYM_NUM, lambda value: input_display.label_keysym_num_display.configure(text=value))
        state.attach(c.KEYCODE, lambda value: input_display.label_keycode_display.configure(text=value))
        input_display.attach_to_switch(lambda on_off: state.toggle_user_input_capture(on_off))

        # Bind commands
        root.bind('<Key>', state.set_text)
        controller_buttons.button_ok['command'] = state.upon_ok
        for check_button in configuration_panel.check_buttons:
            check_button['command'] = lambda *_: state.update_state_upon_configuration()
        configuration_panel.entry_key.bind('<KeyRelease>', lambda *_: state.update_state_upon_configuration())

        root.mainloop()

    def test_encapsulate_as_an_app(self):
        from n_keyboard.app.app import App
        app = App()
        app.run()

    def test_keyboard_display(self):
        from n_keyboard.app.app import App
        app = App()
        app.display_keyboard()
        app.run()


if __name__ == '__main__':
    unittest.main()
