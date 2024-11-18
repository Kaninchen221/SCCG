import logging
from venv import EnvBuilder
from Src.Utils.paths import *
from Src.Utils.subprocess_helpers import log_subprocess, run_subprocess

logging.basicConfig(level=logging.NOTSET)
logger_handle = "Setup"
logger = logging.getLogger(logger_handle)
logger.setLevel(logging.INFO)


def create_venv():
    logger.info('Create VENV')
    venvBuilder = EnvBuilder(False, True, False, False, True)
    venvBuilder.create(".venv")


def create_pth_file():
    site_packages_path = find_venv_site_packages_path()
    SCCG_pth_path = site_packages_path / "SCCG.pth"
    logger.info(f"SCCG pth path: {SCCG_pth_path}")

    with open(SCCG_pth_path, "w") as file:
        src_path = find_root_path() / "Src"
        logger.info(f"Src path: {src_path}")
        file.write(str(src_path))

    assert SCCG_pth_path


def install_requirements():
    requirements_path = find_root_path() / "requirements.txt"
    if not requirements_path.exists():
        raise Exception("requirements.txt file doesn't exist")

    logger.info(f"requirements.txt path: {requirements_path}")
    pip_arguments = "--disable-pip-version-check install -r" + str(requirements_path)
    process = run_subprocess(find_venv_pip_path(), pip_arguments)
    log_subprocess(process, logger)


logger.info('Start')
create_venv()
create_pth_file()
install_requirements()
logger.info('Completed')
