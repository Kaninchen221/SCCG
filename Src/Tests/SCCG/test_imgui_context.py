from SCCG.imgui_context import ImguiContext
from SCCG.window import Window


def test_properties():
    imgui_context = ImguiContext()
    assert imgui_context.imgui_internal_context is None
    assert imgui_context.imgui_io is None
    assert imgui_context.imgui_glfw_renderer is None


def test_init():
    window = Window()
    window.init()

    imgui_context = ImguiContext()
    imgui_context.init(window)
