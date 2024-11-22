import logging

import glfw
import imgui
from imgui.integrations.glfw import GlfwRenderer


class POC:
    def __init__(self):
        self.window = None
        self.io = None
        self.ctx = None
        self.previous_mouse_delta = 0, 0
        self.skip_frames = 0
        self.resize_root_window_only_once_done = False

    def temp_func(self):
        # Initialize the library
        if not glfw.init():
            return

        glfw.window_hint(glfw.DECORATED, False)

        # Create a windowed mode window and its OpenGL context
        self.window = glfw.create_window(640, 480, "Hello World", None, None)
        if not self.window:
            glfw.terminate()
            return

        # initilize imgui context (see documentation)
        self.ctx = imgui.create_context()
        self.io = imgui.get_io()
        self.io.display_size = 640, 480
        self.io.fonts.get_tex_data_as_rgba32()
        self.io.fonts.add_font_default()
        self.io.fonts.texture_id = 0  # set any texture ID to avoid segfaults

        # Make the window's context current
        glfw.make_context_current(self.window)

        imgui_glfw_renderer = GlfwRenderer(self.window, True)

        # Loop until the user closes the window
        while not glfw.window_should_close(self.window):
            # Render here, e.g. using pyOpenGL
            imgui_glfw_renderer.process_inputs()
            self.imgui_test()
            imgui_glfw_renderer.render(imgui.get_draw_data())

            # Swap front and back buffers
            glfw.swap_buffers(self.window)

            # Poll for and process events
            glfw.poll_events()

        glfw.terminate()

    def imgui_test(self):

        imgui.new_frame()

        if not self.resize_root_window_only_once_done:
            # Root imgui window need to be resized to os window
            imgui.set_next_window_position(0, 0)
            imgui.set_next_window_size(self.io.display_size.x, self.io.display_size.y)
            self.resize_root_window_only_once_done = True

        imgui.begin("SCCG", False, imgui.WINDOW_NO_COLLAPSE | imgui.WINDOW_NO_TITLE_BAR)

        if self.resize_root_window_only_once_done:
            imgui_root_window_size = imgui.get_window_size()
            glfw.set_window_size(self.window, int(imgui_root_window_size[0]), int(imgui_root_window_size[1]))

        if imgui.is_mouse_down(1) and self.skip_frames <= 0:
            window_pos = glfw.get_window_pos(self.window)
            mouse_delta = self.io.mouse_delta
            new_position = int(window_pos[0] + mouse_delta[0] * 2), int(window_pos[1] + mouse_delta[1] * 2)

            glfw.set_window_pos(self.window, new_position[0], new_position[1])

            self.previous_mouse_delta = int(mouse_delta[0]), int(mouse_delta[1])
            self.skip_frames = 1
        else:
            self.skip_frames -= 1

        imgui.text("Hello world!")

        imgui.same_line()

        if imgui.button("Close"):
            glfw.set_window_should_close(self.window, True)

        imgui.end()

        imgui.render()
        imgui.end_frame()


if __name__ == '__main__':

    logging.basicConfig(level=logging.NOTSET)
    logger_handle = "Main"
    logger = logging.getLogger(logger_handle)
    logger.setLevel(logging.INFO)

    poc = POC()

    logger.info("Start SCCG")
    try:
        poc.temp_func()
    except Exception as exception:
        print(exception.args)
        exit(1)
