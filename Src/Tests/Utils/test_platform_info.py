from Utils import platform_info


def test_is_platform_name():
    is_windows = platform_info.is_windows()
    is_linux = platform_info.is_linux()
    if is_windows:
        assert not is_linux
    elif is_linux:
        assert not is_windows
    else:
        raise Exception("Not supported platform")



