import json
import tkinter as tk
from typing import Callable

from n_keyboard import constant as c


class State:
    def __init__(self, get_user_input: Callable, path: str = None):
        with open(path, 'r') as json_file:
            try:
                state = json.load(json_file)
            except:
                state = dict()

        self.state = state
        self.path = path
        self.keycode = None
        self._subscribers: dict[[str], list] = {}
        self._capture_user_input = True
        self._get_user_input = get_user_input

    def toggle_user_input_capture(self, on_off: bool):
        self._capture_user_input = on_off

    def attach(self, key: str, subscriber: Callable):
        if key in self._subscribers:
            self._subscribers[key].append(subscriber)
        else:
            self._subscribers[key] = [subscriber]

    def _notify(self, key, value):
        for subscriber in self._subscribers.get(key, []):
            subscriber(value)

    def upon_ok(self):
        clean_state = {}
        for keycode, data in self.state.items():
            if c.USER_INPUT in data:
                clean_state[keycode] = data
        with open(self.path, 'w') as json_file:
            json.dump(clean_state, json_file)
            print(f'Saved file to {self.path}.')

    def update_state_upon_user_input(self, e: tk.Event):
        self.keycode = e.keycode
        new_state = {
            e.keycode: {c.SYSTEM_STATE: {
                c.STATE: e.state,
                c.CHAR: e.char,
                c.KEYSYM: e.keysym,
                c.KEYSYM_NUM: e.keysym_num,
            }}
        }
        self.state.update(new_state)

    def update_state_upon_configuration(self):
        system_state = self.state.get(self.keycode)
        if system_state:
            user_input = self._get_user_input()
            system_state.update({c.USER_INPUT: user_input})
            new_state = {
                self.keycode: system_state,
            }
            self.state.update(new_state)

    def set_text(self, e: tk.Event):
        if self._capture_user_input:
            self._notify(c.STATE, e.state)
            self._notify(c.CHAR, e.char)
            self._notify(c.KEYSYM, e.keysym)
            self._notify(c.KEYSYM_NUM, e.keysym_num)
            self._notify(c.KEYCODE, e.keycode)

            self.update_state_upon_user_input(e)
