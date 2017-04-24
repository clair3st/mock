"""Testing an api."""

import requests
from unittest.mock import patch
from project.services import get_todos


def test_request():
    """Send a request to the API server and store the response."""
    response = requests.get('http://jsonplaceholder.typicode.com/todos')
    assert response.ok


def test_request_response():
    """Call the service which will send a request to the server."""
    response = get_todos()
    assert response is not None


@patch('project.services.requests.get')  # target get requests
def test_getting_todos(mock_get):
    """Configure the mock to return a response with an OK status code."""
    mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
    response = get_todos()

    # If the request is sent successfully, expect a response to be returned.
    assert response is not None
