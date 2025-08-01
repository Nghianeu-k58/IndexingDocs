"""
Test health check api.
"""

from fastapi import status


def test_health_check_api(client):
    url = "/health-check"
    res = client.get(url=url)

    assert res.status_code == status.HTTP_200_OK
    assert res.content == b"OK"
