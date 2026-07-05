"""Logging helpers.

Functions
---------
get_logger_named(logger_name: str) -> Logger
"""

from logging import DEBUG
from logging import getLogger, Formatter, Logger, StreamHandler


def get_logger_named(logger_name: str) -> Logger:
    """Get a logger named logger_name.
    
    Formatter: "{asctime} - {name}:{lineno} - {levelname} - {message}"

    Handlers:
        - StreamHandler
    
    Level: 
        - Logger: DEBUG
        - StreamHandler: DEBUG
    
    Parameters
    ----------
    logger_name: str
        A string representing the logger's name.
    
    Returns
    -------
    Logger
        A logging.Logger object named logger_name.
    """
    logger = getLogger(logger_name)
    logger.handlers.clear()  # https://santos-k.medium.com/solving-duplicate-log-entries-issue-in-python-logging-d4b1cad8e588
    logger.setLevel(DEBUG)

    formatter = Formatter(
        "{asctime} - {name}:{lineno} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M",
    )

    console_handler = StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # file_handler = FileHandler(
    #     filename=f"{logger_name}.log",
    #     mode='a',
    #     encoding='utf-8',
    # )
    # file_handler.setFormatter(formatter)
    # file_handler.setLevel(WARNING)
    # logger.addHandler(file_handler)

    return logger
