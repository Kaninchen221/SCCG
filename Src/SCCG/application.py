import glfw
import imgui
from imgui import Vec2
from imgui.integrations.glfw import GlfwRenderer


class Application:

    def __init__(self):
        self.window = None
        self.window_size = Vec2(640, 480)
        self.imgui_context = None
        self.imgui_io = None
        self.imgui_glfw_renderer = None
        self.resized_root_window_at_start = False
        self.skip_frames_for_root_window_moving = 0

    def start(self):
        while not glfw.window_should_close(self.window):
            glfw.poll_events()

            self._process_imgui()

            glfw.swap_buffers(self.window)

        glfw.terminate()

    def _process_imgui(self):
        self.imgui_glfw_renderer.process_inputs()

        imgui.new_frame()

        self._imgui_root_window()

        imgui.render()
        imgui.end_frame()

        imgui_draw_data = imgui.get_draw_data()
        if imgui_draw_data:
            self.imgui_glfw_renderer.render(imgui.get_draw_data())

    def _imgui_root_window(self):
        if not self.resized_root_window_at_start:
            imgui.set_next_window_position(0, 0)
            imgui.set_next_window_size(self.imgui_io.display_size.x, self.imgui_io.display_size.y)
            self.resized_root_window_at_start = True

        imgui.begin("Root Window", False, imgui.WINDOW_NO_COLLAPSE | imgui.WINDOW_NO_TITLE_BAR)

        if self.resized_root_window_at_start:
            imgui_root_window_size = imgui.get_window_size()
            glfw.set_window_size(self.window, int(imgui_root_window_size[0]), int(imgui_root_window_size[1]))

        if imgui.is_mouse_down(1) and self.skip_frames_for_root_window_moving <= 0:
            window_pos = glfw.get_window_pos(self.window)
            mouse_delta = self.imgui_io.mouse_delta
            new_position = int(window_pos[0] + mouse_delta[0] * 2), int(window_pos[1] + mouse_delta[1] * 2)

            glfw.set_window_pos(self.window, new_position[0], new_position[1])

            self.skip_frames_for_root_window_moving = 1
        else:
            self.skip_frames_for_root_window_moving -= 1

        if imgui.button("Close"):
            glfw.set_window_should_close(self.window, True)

        imgui.end()

    def init(self):
        if not self._init_window():
            return False

        if not self._init_imgui():
            return False

        return True

    def _init_window(self):
        if not glfw.init():
            return False

        # Hide window upper bar
        glfw.window_hint(glfw.DECORATED, False)

        self.window = glfw.create_window(self.window_size.x, self.window_size.y, "Hello World", None, None)
        if not self.window:
            glfw.terminate()
            return False

        glfw.make_context_current(self.window)

        return True

    def _init_imgui(self):
        self.imgui_context = imgui.create_context()
        self.imgui_io = imgui.get_io()
        self.imgui_io.display_size = self.window_size
        self.imgui_io.fonts.get_tex_data_as_rgba32()
        self.imgui_io.fonts.add_font_default()
        # Set any texture ID to avoid segfaults
        self.imgui_io.fonts.texture_id = 0

        self.imgui_glfw_renderer = GlfwRenderer(self.window, True)

        return True
