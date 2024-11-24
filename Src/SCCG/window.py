from imgui import Vec2
import glfw


class Window:

    def __init__(self):
        self.size = Vec2(300, 300)
        self.internal_window = None

    def __del__(self):
        glfw.terminate()

    def init(self):
        if not glfw.init():
            return False

        # Hide window upper bar
        glfw.window_hint(glfw.DECORATED, False)

        self.internal_window = glfw.create_window(self.size.x, self.size.y, "Hello World", None, None)
        if not self.internal_window:
            glfw.terminate()
            return False

        glfw.make_context_current(self.internal_window)

        return True
