import logging
from pathlib import Path

from Src.Utils.subprocess_helpers import log_subprocess, run_subprocess
from Src.Utils.paths import find_venv_pyinstaller_path, find_root_path

logging.basicConfig(level=logging.NOTSET)
logger_handle = "Build"
logger = logging.getLogger(logger_handle)
logger.setLevel(logging.INFO)


def create_exe():
    root_path = find_root_path()
    dist_arg = f"--distpath {root_path / 'deploy/dist'}"
    work_arg = f"--workpath {root_path / 'deploy/temp'}"
    SCCG_path = root_path / "Src/SCCG/__main__.py"

    arguments = f"{SCCG_path} --clean --onefile --name SCCG {dist_arg} {work_arg}"
    process = run_subprocess(find_venv_pyinstaller_path(), arguments)
    log_subprocess(process, logger)


create_exe()
