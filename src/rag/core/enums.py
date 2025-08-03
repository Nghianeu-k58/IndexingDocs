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

    user_name = "ELASTIC_USERNAME"
    password = "ELASTIC_PASSWORD"
    verify_certs = "ELASTIC_VERIFY_CERTS"
    mapping_version = "ELASTIC_MAPPING_VERSION"
    connection_scheme = "ELASTIC_SCHEME_CONNNECTION"
