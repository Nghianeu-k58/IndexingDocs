"""
Define all test of user.
"""

from fastapi import status

from src.rag.user.enums import UserField

USER_URL = "/api/v1/users"


def test_create_user_successful(client, es_connection):
    test_email = "test_user@example.com"
    payload = {
        UserField.email: test_email,
        UserField.password: "Testpass123",
        UserField.name: "Test name",
    }
    res = client.post(url=USER_URL, json=payload)

    assert res.status_code == status.HTTP_201_CREATED
    assert res.json()["msg"] == f"Create user with email {test_email} successful."

    user_record = es_connection.search(
        index="user", body={"query": {"match": {"email": test_email}}}
    )
    assert len(user_record["hits"]["hits"]) != 0


def test_create_user_already_existed(client, users_data):
    test_email = "test_user1@example.com"
    payload = {
        UserField.email: test_email,
        UserField.password: "Testpass123",
        UserField.name: "Test name",
    }
    res = client.post(url=USER_URL, json=payload)

    assert res.status_code == status.HTTP_400_BAD_REQUEST
    assert res.json()["msg"] == f"User with email {test_email} already existed."


def test_create_user_with_invalid_email(client):
    test_email = "test_userexample.com"
    payload = {
        UserField.email: test_email,
        UserField.password: "Testpass123",
        UserField.name: "Test name",
    }
    res = client.post(url=USER_URL, json=payload)

    assert res.status_code == status.HTTP_400_BAD_REQUEST
    assert res.json()["msg"] == 'Email must contains "@" symbol.'
