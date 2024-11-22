import logging

from SCCG.application import Application


if __name__ == '__main__':

    logging.basicConfig(level=logging.NOTSET)
    logger_handle = "Main"
    logger = logging.getLogger(logger_handle)
    logger.setLevel(logging.INFO)

    application = Application()

    logger.info("Start SCCG")
    try:
        application.init()
        application.start()
    except Exception as exception:
        print(exception.args)
        exit(1)
