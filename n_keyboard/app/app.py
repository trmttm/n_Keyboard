from n_keyboard.gui.bind_commands import bind_commands
from n_keyboard.gui.components.configuration_panel import ConfigurationPanel
from n_keyboard.gui.components.controller_buttons import ControllerButtons
from n_keyboard.gui.components.keyboard import Keyboard
from n_keyboard.gui.components.keyboard_input_display import KeyboardInputDisplay
from n_keyboard.gui.components.parent_frame import ParentFrame
from n_keyboard.gui.components.root import instantiate_root
from .define_objects_interactions import define_objects_interactions
from .gui_state import instantiate_state


class App:
    def __init__(self, root=None):
        if root is None:  # root may be toplevel, passed by client application.
            root = instantiate_root()
        self._root = root

        self._load_gui()
        self._instantiate_state()
        self._define_objects_interactions()
        self._bind_commands()

    def _load_gui(self):
        # Each GUI components positions are hardcoded in their constructor.
        self._parent_frame = parent_frame = ParentFrame(self._root)
        self._input_display = KeyboardInputDisplay(parent_frame)
        self._configuration_panel = ConfigurationPanel(parent_frame)
        self._controller_buttons = ControllerButtons(parent_frame)

    def _instantiate_state(self):
        self._state = instantiate_state(self._configuration_panel)

    def _define_objects_interactions(self):
        define_objects_interactions(self._input_display, self._state)

    def _bind_commands(self):
        bind_commands(self._configuration_panel, self._controller_buttons, self._root, self._state)

    def display_keyboard(self):
        Keyboard(self._parent_frame)
        self._controller_buttons.grid(row=2, column=0, columnspan=2)

    def run(self):
        self._root.mainloop()
