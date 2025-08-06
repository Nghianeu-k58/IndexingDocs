"""
Define all enums that user for all system.
"""

DATETIME_FORMAT = "%Y-%m-%d %H-%M-%S"


class HashAlgorithms:
    md5 = "MD5"
    sha256 = "SHA256"
    sha512 = "SHA512"


class UserFields:
    email = "email"
    user_id = "user_id"
    role = "role"


class SystemENV:
    logging_mode = "LOGGING_MODE"
    api_key = "API_KEY"
    algorithm = "ALGORITHM"
    expire_day = "EXPIRE_DAYS"


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
