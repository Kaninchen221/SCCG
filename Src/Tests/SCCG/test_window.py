from SCCG.window import Window


def test_window_init():
    window = Window()
    # I'm only using free runners (github actions) and these don't have a GPU
    # window.init()

    assert window.internal_window is None
