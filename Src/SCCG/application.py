import glfw
import imgui

from SCCG.imgui_context import ImguiContext
from SCCG.imgui_root_window import ImguiRootWindow
from SCCG.window import Window


class Application:

    def __init__(self):
        self.window = Window()
        self.imgui_root_window = ImguiRootWindow()
        self.imgui_context = ImguiContext()

    def start(self):
        while not glfw.window_should_close(self.window.internal_window):
            glfw.poll_events()

            self._process_imgui()

            glfw.swap_buffers(self.window.internal_window)

        glfw.terminate()

    def _process_imgui(self):
        self.imgui_context.glfw_renderer.process_inputs()

        imgui.new_frame()

        self.imgui_root_window.process_imgui()

        imgui.render()
        imgui.end_frame()

        imgui_draw_data = imgui.get_draw_data()
        if imgui_draw_data:
            self.imgui_context.glfw_renderer.render(imgui.get_draw_data())

    def init(self, init_window: bool = True):
        if init_window:
            if not self.window.init():
                return False

        if init_window:
            self.imgui_context.init(self.window)
        else:
            self.imgui_context.init(None)

        self.imgui_root_window.init(self.imgui_context.io, self.window)

        return True
