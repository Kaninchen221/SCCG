import logging


if __name__ == '__main__':

    logging.basicConfig(level=logging.NOTSET)
    logger_handle = "Main"
    logger = logging.getLogger(logger_handle)
    logger.setLevel(logging.INFO)

    logger.info("Start SCCG")
    try:
        pass
    except Exception as exception:
        print(exception.args)
        exit(1)
