from n_keyboard.gui.components.configuration_panel import ConfigurationPanel
from n_keyboard.gui.components.controller_buttons import ControllerButtons
from n_keyboard.gui.components.keyboard_input_display import KeyboardInputDisplay
from tests.test import instantiate_root
from .bind_commands import bind_commands
from .define_objects_interactions import define_objects_interactions
from .gui_state import instantiate_state
from .parent_frame import configure_frame_parent


class App:
    def __init__(self, root=None):
        if root is None:  # root may be toplevel, passed by client application.
            root = instantiate_root()
        self._root = root

        self._load_gui()
        self._instantiate_state()
        self._define_objects_interactions()
        self._bind_commands()
        self._root.mainloop()

    def _load_gui(self):
        frame_parent = configure_frame_parent(self._root)
        self._input_display = KeyboardInputDisplay(frame_parent)
        self._configuration_panel = ConfigurationPanel(frame_parent, column=1)
        self._controller_buttons = ControllerButtons(frame_parent, row=1, columnspan=2)

    def _instantiate_state(self):
        self._state = instantiate_state(self._configuration_panel)

    def _define_objects_interactions(self):
        define_objects_interactions(self._input_display, self._state)

    def _bind_commands(self):
        bind_commands(self._configuration_panel, self._controller_buttons, self._root, self._state)
