
#from typing import Iterable

from typing import Any
from todo_app.debugger import writelog
from todo_app.ItemClass import Item
from dotenv import load_dotenv, find_dotenv
import os

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
        TRELLO_TODO_ID = os.getenv('TRELLO_TODO_ID')
        context = 'ViewModelClass.py todo_items'
        doing = 'todo_items'
        todo_items_list = [item for item in self._items if item.idList == TRELLO_TODO_ID ]
        return todo_items_list      
    
    @property
    def doin_items(self):
        TRELLO_DOIN_ID = os.getenv('TRELLO_DOIN_ID')
        context = 'ViewModelClass.py doin_items'
        doing = 'doin_items'
        doin_items_list = [item for item in self._items if item.idList == TRELLO_DOIN_ID ]
        return doin_items_list   
    
    @property
    def done_items(self):
        TRELLO_DONE_ID = os.getenv('TRELLO_DONE_ID')
        context = 'ViewModelClass.py done_items'
        doing = 'done_items'
        done_items_list = [item for item in self._items if item.idList == TRELLO_DONE_ID ]
        return done_items_list

 
    


    