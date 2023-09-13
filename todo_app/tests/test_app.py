import os
import pytest
import requests
from todo_app.app import create_app, test_func
from dotenv import load_dotenv, find_dotenv
from todo_app.data.config import TRELLO_BOARD_ID
from todo_app.debugger import writelog

# file_path = find_dotenv('.env.test')
# load_dotenv(file_path, override=True)

@pytest.fixture
def client():

        context = 'test_app.py pytest fixture'
        doing = 'app.create_app()'
        # Use our test integration config instead of the 'real' version
        file_path = find_dotenv('.env.test')
        #file_path = find_dotenv('.test')
        writelog(context, doing, 'file_path', file_path)
        load_dotenv(file_path, override=True)

        # Create the new app.
        test_app = create_app()
        #test_app = current_app.create_app()
        writelog(context, doing, 'test_app', test_app)

        # Use the app to create a test_client that can be used in our tests.
        with test_app.test_client() as client: 
            yield client

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data

# Stub replacement for requests.get(url)
#def stub(url, params={}, headers=None): #headers = { "Accept": "application/json" }
def stub(method, url, params={}, headers=None): #headers = { "Accept": "application/json" }
    #test_board_id = os.environ.get('TRELLO_BOARD_ID')
    test_board_id = TRELLO_BOARD_ID
    fake_response_data = None
    if url == f'https://api.trello.com/1/boards/{test_board_id}/lists':
        fake_response_data = [{
            'id': '123abc',
            'name': 'To Do',
            'cards': [{'id': '456', 'name': 'Test card', 'idList': '64ae6f476f946f8c451a5cb9'}]
        }]
        return StubResponse(fake_response_data)
#items.append(Item(item['id'], item['name'], item['idList']))
    raise Exception(f'Integration test did not expect URL "{url}"')


def test_index_page(monkeypatch, client):
        # Replace requests.get(url) with our own function
        #monkeypatch.setattr(requests, 'get', stub)
        monkeypatch.setattr(requests, 'request', stub)

        # Make a request to our app's index page
        response = client.get('/')

        assert response.status_code == 200
        assert 'Test card' in response.data.decode()