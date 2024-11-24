import imgui
from imgui.integrations.glfw import GlfwRenderer

from SCCG.window import Window


class ImguiContext:

    def __init__(self):
        self.imgui_internal_context = None
        self.imgui_io = None
        self.imgui_glfw_renderer = None

    def init(self, window: Window):
        self.imgui_internal_context = imgui.create_context()
        self.imgui_io = imgui.get_io()
        self.imgui_io.display_size = window.size
        self.imgui_io.fonts.get_tex_data_as_rgba32()
        self.imgui_io.fonts.add_font_default()
        # It was in a tutorial from the first result in google, but I don't trust google tutorials
        # self.imgui_io.fonts.texture_id = 0

        if window is not None:
            self.imgui_glfw_renderer = GlfwRenderer(window.internal_window, True)
