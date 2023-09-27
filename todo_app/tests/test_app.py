import os, pytest, requests
from todo_app.data.trello import get_trello_cards
from todo_app.app import create_app, test_func
from dotenv import load_dotenv, find_dotenv
from todo_app.debugger import writelog

file_path = find_dotenv('tests/.env.test')
load_dotenv(file_path, override=True)

TRELLO_BOARD_ID = os.getenv('TRELLO_BOARD_ID') 
TRELLO_TODO_ID = os.getenv('TRELLO_TODO_ID') 

@pytest.fixture
def client():

        context = 'test_app.py pytest fixture'
        doing = 'app.create_app()'

        # Create the new app.
        test_app = create_app()
        #test_app = current_app.create_app()

        # Use the app to create a test_client that can be used in our tests.
        with test_app.test_client() as client: 
            yield client

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data

# Stub replacement for requests.get(url)
def stub(method, url, params={}, headers=None): #headers = { "Accept": "application/json" }
    test_board_id = TRELLO_BOARD_ID
    context = 'test_app.py stub()'
    doing = 'url'
    writelog(context, doing, 'test_board_id', test_board_id)
    fake_response_data = None
    writelog(context, doing, 'url', url)
    if url == f'https://api.trello.com/1/boards/{test_board_id}/lists':
        fake_response_data = [{
            'id': '123abc',
            'name': 'To Do',
            'cards': [{'id': '456', 'name': 'Test card', 'idList': TRELLO_TODO_ID}]
        }]
        return StubResponse(fake_response_data)
    raise Exception(f'Integration test did not expect URL "{url}"')

def test_index_page(monkeypatch, client):
    # Replace requests.get(url) with our own function
    monkeypatch.setattr(requests, 'request', stub)

    # Make a request to our app's index page
    response = client.get('/')

    assert response.status_code == 200
    assert 'Test card' in response.data.decode()