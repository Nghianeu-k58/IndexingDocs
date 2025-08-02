"""
Define all enums that user for all system.
"""


class SystemEnvironmentVariable:
    logging_mode = "LOGGING_MODE"


class LoggingMode:
    debug = "DEBUG"
    warning = "WARNING"
    info = "INFO"


class ElasticENV:
    host = "ELASTIC_HOST"
    port = "ELASTIC_PORT"
