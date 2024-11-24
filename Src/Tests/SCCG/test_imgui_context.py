from SCCG.imgui_context import ImguiContext
from SCCG.window import Window


def test_properties():
    imgui_context = ImguiContext()
    assert imgui_context.internal_context is None
    assert imgui_context.io is None
    assert imgui_context.glfw_renderer is None


def test_init():
    imgui_context = ImguiContext()
    imgui_context.init(None)
