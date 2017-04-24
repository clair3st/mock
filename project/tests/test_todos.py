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


def test_getting_todos_again():
    """Explicitly patch a function within a block of code.

    using a context manager. The with statement patches a function used by any
    code in the code block. When the code block ends, the original function is
    restored.
    """
    with patch('project.services.requests.get') as mock_get:
        # Configure the mock to return a response with an OK status code.
        mock_get.return_value.ok = True

        # Call the service, which will send a request to the server.
        response = get_todos()

    # If the request is sent successfully, expect a response to be returned.
    assert response is not None


def test_getting_todos_again_again():
    """Another way to patch a function is to use a patcher.

    Here, I identify the source to patch, and then I explicitly start using
    the mock. The patching does not stop until I explicitly tell the system
    to stop using the mock.
    """
    mock_get_patcher = patch('project.services.requests.get')

    # Start patching `requests.get`.
    mock_get = mock_get_patcher.start()

    # Configure the mock to return a response with an OK status code.
    mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
    response = get_todos()

    # Stop patching `requests.get`.
    mock_get_patcher.stop()

    # If the request is sent successfully, expect a response to be returned.
    assert response is not None
