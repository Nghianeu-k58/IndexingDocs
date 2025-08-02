"""
Test for wait for ElasticSearch database.
"""

from fastapi import status
from elasticsearch.exceptions import ConnectionError as ElasticConnectionError
from requests.exceptions import ConnectionError as RequestsConnectionError
from unittest.mock import patch, MagicMock

from src.rag.dataaccess.migrations.elasticsearch.wait_for_elastic import (
    wait_for_elastic_search,
)
from tests.rag.conftest import ELASTIC_HOST_FAKE, ELASTIC_PORT_FAKE


URL = f"http://{ELASTIC_HOST_FAKE}:{ELASTIC_PORT_FAKE}/_cluster/health"


@patch("src.rag.dataaccess.migrations.elasticsearch.wait_for_elastic.requests")
def test_wait_for_elastic_ready(patched_request):
    mock_response = MagicMock()
    mock_response.status_code = status.HTTP_200_OK

    patched_request.return_value = mock_response

    wait_for_elastic_search()
    patched_request.get.assert_called_once_with(url=URL)


@patch("time.sleep")
@patch("src.rag.dataaccess.migrations.elasticsearch.wait_for_elastic.requests")
def test_wait_for_elastic_delay(patched_request, patched_time):
    mock_response = MagicMock()
    mock_response.status_code = status.HTTP_200_OK
    patched_request.side_effect = [
        RequestsConnectionError,
        ElasticConnectionError,
        mock_response,
    ]
    wait_for_elastic_search()
    patched_request.get.call_count == 3
