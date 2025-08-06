"""
Define helper functions using for all components.
"""

from hashlib import md5, sha256, sha512
from src.rag.core.enums import HashAlgorithms
from src.rag.core.logger import logger

ALGORITHMS = {
    HashAlgorithms.md5: md5,
    HashAlgorithms.sha256: sha256,
    HashAlgorithms.sha512: sha512,
}


def generate_id(algorithm: str, *args):
    """Generate and return hash id"""
    RESPONSE_ERROR = (
        "The algorithm does not support! Please try again with MD5, SHA256 or SHA512."
    )
    func = ALGORITHMS.get(algorithm, None)
    if not func:
        logger.warning(RESPONSE_ERROR)
        return None
    params = [str(v) for v in args]
    return func("".join(params).encode()).hexdigest()
