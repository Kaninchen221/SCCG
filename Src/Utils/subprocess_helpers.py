import subprocess


def log_subprocess(process, logger):
    if process.stdout:
        logger.info(process.stdout)

    if process.stderr:
        logger.info(process.stderr)

    if process.returncode != 0:
        raise Exception(str(process.stdout) + str(process.stderr))


def run_subprocess(program_path, args, use_shell=True, use_universal_newlines=True):
    process = subprocess.run(f"{program_path} {args}", stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             shell=use_shell,
                             universal_newlines=use_universal_newlines)
    return process
