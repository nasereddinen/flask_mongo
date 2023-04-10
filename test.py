import pytest
from app import app, db, todos

# Create a test client using the Flask application configured for testing
@pytest.fixture
def client():
    # Create a test client using the Flask application configured for testing pytest uses this to create a test client
    client = app.test_client()

    with app.app_context():
        # Set up test database
        db.drop_collection('todos')
        todos.insert_many([
            {'content': 'todo1', 'degree': ''},
            {'content': 'todo2', 'degree': '.'},
            {'content': 'todo3', 'degree': 'important'}
        ])

    yield client


def test_index(client):
    # Test that the index page returns a 200 status code and displays all todos
    response = client.get('/')
    assert response.status_code == 200
    assert b'todo1' in response.data
    assert b'todo2' in response.data
    assert b'todo3' in response.data


def test_add_todo(client):
    # Test that adding a new todo to the database works correctly
    response = client.post('/', data={'content': 'new todo', 'degree': 'unimportant'})
    assert response.status_code == 302  # redirected to index page
    assert todos.count_documents({'content': 'new todo'}) == 1


def test_delete(client):
    # Test that deleting a todo from the database works correctly
    todo = todos.find_one({'content': 'todo2'})
    response = client.post(f'/{todo["_id"]}/delete/')
    assert response.status_code == 302  # redirected to index page
    assert todos.count_documents({'content': 'todo2'}) == 0
