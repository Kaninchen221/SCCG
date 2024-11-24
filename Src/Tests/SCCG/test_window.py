from SCCG.window import Window


def test_window_init():
    window = Window()
    window.init()

    assert window.internal_window is not None
