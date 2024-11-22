from SCCG.application import Application
import pytest


def test_application_init():
    application = Application()
    init_result = application.init()

    assert application.window is not None
    assert application.imgui_context is not None
    assert application.imgui_io is not None
    assert application.imgui_glfw_renderer is not None
    assert init_result
