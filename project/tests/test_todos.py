"""Testing an api."""

import requests
from unittest.mock import Mock, patch
from project.services import get_todos, get_uncompleted_todos


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


@patch('project.services.requests.get')
def test_getting_todos_when_response_is_ok(mock_get):
    """Use a mock to test functionality of todos.

    whenever the return_value is added to a mock, that mock is modified to be
    run as a function, and by default it returns another mock object.
    """
    todos = [{
        'userId': 1,
        'id': 1,
        'title': 'Make the bed',
        'completed': False
    }]

    # Configure the mock to return a response with an OK status code.
    mock_get.return_value = Mock(ok=True)
    # Also, the mock should have a `json()` method that returns list of todos.
    mock_get.return_value.json.return_value = todos

    # Call the service, which will send a request to the server.
    response = get_todos()

    # If the request is sent successfully, expect a response to be returned.
    assert response.json() == todos


@patch('project.services.requests.get')
def test_getting_todos_when_response_is_not_ok(mock_get):
    """Test negative."""
    # Configure the mock to not return a response with an OK status code.
    mock_get.return_value.ok = False

    # Call the service, which will send a request to the server.
    response = get_todos()

    # If the response contains an error, I should get no todos.
    assert response is None


@patch('project.services.get_todos')
def test_getting_uncompleted_todos_when_todos_is_not_none(mock_get_todos):
    """Test ability to filter response."""
    todo1 = {
        'userId': 1,
        'id': 1,
        'title': 'Make the bed',
        'completed': False
    }
    todo2 = {
        'userId': 1,
        'id': 2,
        'title': 'Walk the dog',
        'completed': True
    }

    # Configure mock to return a response with a JSON-serialized list of todos.
    mock_get_todos.return_value = Mock()
    mock_get_todos.return_value.json.return_value = [todo1, todo2]

    # Call the service, which will get a list of todos filtered on completed.
    uncompleted_todos = get_uncompleted_todos()

    # Confirm that the mock was called.
    assert mock_get_todos.called

    # Confirm that the expected filtered list of todos was returned.
    assert uncompleted_todos == [todo1]


@patch('project.services.get_todos')
def test_getting_uncompleted_todos_when_todos_is_none(mock_get_todos):
    """Test getting uncomplete todos."""
    # Configure mock to return None.
    mock_get_todos.return_value = None

    # Call the service, which will return an empty list.
    uncompleted_todos = get_uncompleted_todos()

    # Confirm that the mock was called.
    assert mock_get_todos.called

    # Confirm that an empty list was returned.
    assert uncompleted_todos == []
