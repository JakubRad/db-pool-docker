import logging
import sys


def init_logger(name: str = None, level: str = None) -> "logging.Logger":
    """
    Basic logger with timestamp.
    """

    formatter = logging.Formatter(
        fmt="%(asctime)-15s %(levelname)s %(name)s %(message)s"
    )
    handler_stream = logging.StreamHandler(sys.stdout)
    handler_stream.setFormatter(formatter)

    logger = logging.getLogger(name=name or "[task_3_app]")

    if not logger.handlers:
        logger.addHandler(handler_stream)

    logger.setLevel(level=level or logging.INFO)

    logger.propagate = False

    return logger
