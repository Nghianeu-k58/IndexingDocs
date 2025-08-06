"""
Define logic for user services.
"""
from datetime import datetime

from elasticsearch import Elasticsearch

from src.rag.core.logger import logger
from src.rag.core.enums import HashAlgorithms
from src.rag.core.utils import generate_id
from src.rag.user.enums import UserField, Role
from src.rag.auth.services import bcrypt_context
from src.rag.dataaccess.migrations.elasticsearch.enums import ElasticsearchIndies


def create_user_logic(usre_data: dict, es_conn: Elasticsearch):
    """Define logic for create user."""
    logger.info(f"Start create user with email: {usre_data[UserField.email]} ...")
    logger.info("Check user existed or not in database ...")
    user_record = es_conn.search(
        index=ElasticsearchIndies.user,
        body={"query": {"match": {"email": usre_data[UserField.email]}}},
    )
    if len(user_record["hits"]["hits"]) != 0:
        return False, f"User with email {usre_data[UserField.email]} already existed."

    es_conn.index(
        index=ElasticsearchIndies.user,
        document={
            UserField.user_id: generate_id(HashAlgorithms.sha256, usre_data[UserField.email]),
            UserField.email: usre_data[UserField.email],
            UserField.password: bcrypt_context.hash(usre_data[UserField.password]),
            UserField.role: Role.user,
            UserField.name: usre_data[UserField.name],
            UserField.created_date: datetime.now().isoformat()
        }
    )
    es_conn.indices.refresh(index=ElasticsearchIndies.user)
    return True, f"Create user with email {usre_data[UserField.email]} successful."
