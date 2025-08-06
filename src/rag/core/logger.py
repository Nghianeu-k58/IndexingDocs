"""
Define logger
"""

import os
import logging

from src.rag.core.enums import LoggingMode, SystemENV

logging.basicConfig(format="%(asctime)s %(name)s %(levelname)s %(message)s")
logger = logging.getLogger()


LOGGING_MODE = {
    LoggingMode.debug: logging.DEBUG,
    LoggingMode.info: logging.INFO,
    LoggingMode.warning: logging.WARNING,
}


def setup_logger_mode(mode: str):
    """Setup and return mode for environment."""
    logger_mode = LOGGING_MODE.get(mode, None)
    if not logger_mode:
        logger.info(f"Cannot find {mode} in LOGGING_MODE. Return default mode.")
        return LOGGING_MODE[LoggingMode.debug]
    logger.info(f"Setup logging mode with level: {mode}")
    return logger_mode


logger_mode = setup_logger_mode(mode=os.environ.get(SystemENV.logging_mode))
logger.setLevel(logger_mode)
