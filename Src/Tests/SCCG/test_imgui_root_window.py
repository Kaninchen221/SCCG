import imgui
from imgui import Vec2

from SCCG.imgui_context import ImguiContext
from SCCG.imgui_root_window import ImguiRootWindow
from SCCG.window import Window


def test_properties():
    imgui_root_window = ImguiRootWindow()
    assert imgui_root_window.name is not None
    assert imgui_root_window.resized_root_window_at_start is not None
    assert imgui_root_window.skip_frames_window_moving is not None
    assert imgui_root_window.imgui_io is None
    assert imgui_root_window.window is None
    assert imgui_root_window.moving_window_speed_modifier is not None


def test_process_imgui():
    window = Window()

    imgui_context = ImguiContext()
    imgui_context.init(None)

    imgui.new_frame()

    imgui_root_window = ImguiRootWindow()
    imgui_root_window.init(imgui_context.io, window)
    imgui_root_window.process_imgui()

    imgui.render()
    imgui.end_frame()
