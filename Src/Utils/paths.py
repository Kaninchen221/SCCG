import os
from pathlib import Path
import platform


def is_root_path(path):
    if not (path / "setup.py").exists():
        return False
    if not (path / "LICENSE").exists():
        return False
    return True


def find_root_path():
    root_path = Path('.').absolute()
    if is_root_path(root_path):
        return root_path

    for parent in root_path.parents:
        if is_root_path(parent):
            return parent

    return None


def find_venv_path():
    return find_root_path() / ".venv"


def find_venv_scripts_path():
    if platform.system() == "Windows":
        scripts_folder = find_venv_path() / "Scripts"
    elif platform.system() == "Linux":
        scripts_folder = find_venv_path() / "bin"
    else:
        raise Exception("Not supported os")
    return scripts_folder


def find_venv_activate_path():
    if platform.system() == "Windows":
        activate_path = find_venv_scripts_path() / "activate.bat"
    elif platform.system() == "Linux":
        activate_path = find_venv_scripts_path() / "activate"
    else:
        raise Exception("Not supported os")
    return activate_path


def find_venv_python_path():
    if platform.system() == "Windows":
        python_path = find_venv_scripts_path() / "python.exe"
    elif platform.system() == "Linux":
        python_path = find_venv_scripts_path() / "python3"
    else:
        raise Exception("Not supported os")
    return python_path


def find_venv_pip_path():
    if platform.system() == "Windows":
        pip_path = find_venv_scripts_path() / "pip.exe"
    elif platform.system() == "Linux":
        pip_path = find_venv_scripts_path() / "pip3"
    else:
        raise Exception("Not supported os")
    return pip_path


def find_venv_lib_path():
    if platform.system() == "Windows":
        pip_path = find_venv_path() / "Lib"
    elif platform.system() == "Linux":
        pip_path = find_venv_scripts_path() / "Lib"
    else:
        raise Exception("Not supported os")
    return pip_path


def find_venv_site_packages_path():
    for subdir, directories, files in os.walk(find_venv_lib_path()):
        for directory in directories:
            path = Path(str(os.path.join(subdir, directory)))
            if path.name == "site-packages":
                return path
    raise Exception("Can't find site-packages path")
