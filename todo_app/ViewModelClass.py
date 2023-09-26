
#from typing import Iterable

from typing import Any
from todo_app.debugger import writelog
from todo_app.ItemClass import Item
from dotenv import load_dotenv, find_dotenv
import os

#file_path = find_dotenv('tests/.env.test')     # test works!
file_path = find_dotenv('.env')                 # app works!
load_dotenv(file_path, override=True)

TRELLO_TODO_ID = os.getenv('TRELLO_TODO_ID')
TRELLO_DOIN_ID = os.getenv('TRELLO_DOIN_ID')
TRELLO_DONE_ID = os.getenv('TRELLO_DONE_ID')

class ViewModel:
    def __init__(self, items):
        self._items = items
 
    @property
    def items(self):
        return self._items

    def __getitem__(self, key): # this allows getting an element (overrided method)
        return self._items[key]
    
    @property
    def todo_items(self):
        context = 'ViewModelClass.py todo_items'
        doing = 'todo_items'
        todo_items_list = [item for item in self._items if item.idList == TRELLO_TODO_ID ]
        return todo_items_list      
    
    @property
    def doin_items(self):
        context = 'ViewModelClass.py doin_items'
        doing = 'doin_items'
        doin_items_list = [item for item in self._items if item.idList == TRELLO_DOIN_ID ]
        return doin_items_list   
    
    @property
    def done_items(self):
        context = 'ViewModelClass.py done_items'
        doing = 'done_items'
        done_items_list = [item for item in self._items if item.idList == TRELLO_DONE_ID ]
        return done_items_list

 
    


    