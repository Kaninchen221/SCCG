import imgui
import glfw

from SCCG.window import Window


class ImguiRootWindow:

    def __init__(self):
        self.name = "Root Window"
        self.resized_root_window_at_start = False
        self.skip_frames_window_moving = 0
        self.skip_frames_window_moving_default = 1
        self.imgui_io = None
        self.window = None
        self.moving_window_speed_modifier = 2

    def init(self, io, window: Window):
        self.imgui_io = io
        self.window = window

    def process_imgui(self):

        if not self.resized_root_window_at_start:
            imgui.set_next_window_position(0, 0)
            imgui.set_next_window_size(self.imgui_io.display_size.x, self.imgui_io.display_size.y)
            self.resized_root_window_at_start = True

        imgui.begin(self.name, False, imgui.WINDOW_NO_COLLAPSE | imgui.WINDOW_NO_TITLE_BAR | imgui.WINDOW_NO_MOVE)

        if self.resized_root_window_at_start:
            imgui_root_window_size = imgui.get_window_size()
            glfw.set_window_size(self.window.internal_window, int(imgui_root_window_size[0]), int(imgui_root_window_size[1]))

        if imgui.is_mouse_down(imgui.MOUSE_BUTTON_RIGHT) and self.skip_frames_window_moving <= 0:
            window_pos = glfw.get_window_pos(self.window.internal_window)
            mouse_delta = self.imgui_io.mouse_delta
            new_position = (int(window_pos[0] + mouse_delta[0] * self.moving_window_speed_modifier),
                            int(window_pos[1] + mouse_delta[1] * self.moving_window_speed_modifier))

            glfw.set_window_pos(self.window.internal_window, new_position[0], new_position[1])

            self.skip_frames_window_moving = self.skip_frames_window_moving_default
        else:
            self.skip_frames_window_moving -= 1

        if imgui.button("Close"):
            glfw.set_window_should_close(self.window, True)

        imgui.end()
