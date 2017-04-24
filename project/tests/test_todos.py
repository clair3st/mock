"""Testing an api."""

import requests
from project.services import get_todos


def test_request():
    """Send a request to the API server and store the response."""
    response = requests.get('http://jsonplaceholder.typicode.com/todos')
    assert response.ok


def test_request_response():
    """Call the service which will send a request to the server."""
    response = get_todos()
    assert response is not None
