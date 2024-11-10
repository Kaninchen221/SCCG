from Utils import paths, platform_info


class TestUtilities:
    def test_zinet_root_path(self):
        root_path = paths.find_root_path()
        assert root_path
        assert root_path.exists()

    def test_find_venv_folder(self):
        actual = paths.find_venv_path()
        expected = paths.find_root_path() / ".venv"
        assert actual == expected

    def test_find_venv_scripts_folder(self):
        venv_scripts_folder = paths.find_venv_scripts_path()

        if platform_info.is_windows():
            expected = paths.find_venv_path() / "Scripts"
        elif platform_info.is_linux():
            expected = paths.find_venv_path() / "bin"
        else:
            raise Exception("Not supported os")

        assert venv_scripts_folder.exists()
        assert venv_scripts_folder == expected

    def test_find_venv_activate_path(self):
        venv_activate_path = paths.find_venv_activate_path()

        if platform_info.is_windows():
            expected = paths.find_venv_scripts_path() / "activate.bat"
        elif platform_info.is_linux():
            expected = paths.find_venv_scripts_path() / "activate"
        else:
            raise Exception("Not supported os")

        assert venv_activate_path.exists()
        assert venv_activate_path == expected

    def test_find_venv_python_path(self):
        venv_python_path = paths.find_venv_python_path()

        if platform_info.is_windows():
            expected = paths.find_venv_path() / "Scripts/python.exe"
        elif platform_info.is_linux():
            expected = paths.find_venv_path() / "bin/python3"
        else:
            raise Exception("Not supported os")

        assert venv_python_path.exists()
        assert venv_python_path == expected

    def test_find_venv_pip_path(self):
        venv_pip_path = paths.find_venv_pip_path()

        if platform_info.is_windows():
            expected = paths.find_venv_path() / "Scripts/pip.exe"
        elif platform_info.is_linux():
            expected = paths.find_venv_path() / "bin/pip3"
        else:
            raise Exception("Not supported os")

        assert venv_pip_path.exists()
        assert venv_pip_path == expected

    def test_find_venv_lib_path(self):
        lib_path = paths.find_venv_lib_path()

        if platform_info.is_windows():
            expected = paths.find_venv_path() / "Lib"
        elif platform_info.is_linux():
            expected = paths.find_venv_path() / "Lib"
        else:
            raise Exception("Not supported os")

        assert lib_path.exists()
        assert lib_path == expected

    def test_find_venv_site_packages_path(self):
        site_packages_path = paths.find_venv_site_packages_path()

        if platform_info.is_windows():
            expected = paths.find_venv_lib_path() / "site-packages"
        elif platform_info.is_linux():
            expected = paths.find_venv_lib_path() / "site-packages"
        else:
            raise Exception("Not supported os")

        assert site_packages_path.exists()
        assert site_packages_path == expected
