from n_keyboard.gui.bind_commands import bind_commands
from n_keyboard.gui.components.configuration_panel import ConfigurationPanel
from n_keyboard.gui.components.controller_buttons import ControllerButtons
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
        frame_parent = ParentFrame(self._root)
        self._input_display = KeyboardInputDisplay(frame_parent)
        self._configuration_panel = ConfigurationPanel(frame_parent)
        self._controller_buttons = ControllerButtons(frame_parent)

    def _instantiate_state(self):
        self._state = instantiate_state(self._configuration_panel)

    def _define_objects_interactions(self):
        define_objects_interactions(self._input_display, self._state)

    def _bind_commands(self):
        bind_commands(self._configuration_panel, self._controller_buttons, self._root, self._state)

    def display_keyboard(self):
        pass

    def run(self):
        self._root.mainloop()
