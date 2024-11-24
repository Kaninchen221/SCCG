import imgui
from imgui import Vec2
from imgui.integrations.glfw import GlfwRenderer

from SCCG.window import Window


class ImguiContext:

    def __init__(self):
        self.internal_context = None
        self.io = None
        self.glfw_renderer = None

    def init(self, window: Window = None):
        self.internal_context = imgui.create_context()
        self.io = imgui.get_io()
        self.io.fonts.get_tex_data_as_rgba32()
        self.io.fonts.add_font_default()
        # It was in a tutorial from the first result in google, but I don't trust google tutorials
        # self.imgui_io.fonts.texture_id = 0

        if window is not None:
            self.io.display_size = window.size
            self.glfw_renderer = GlfwRenderer(window.internal_window, True)
        else:
            self.io.display_size = Vec2(1, 1)
