from SCCG.application import Application
from SCCG.imgui_context import ImguiContext


def test_application_init():
    application = Application()
    init_result = application.init(False)

    assert application.window is not None
    assert type(application.imgui_context) is ImguiContext
    assert init_result
