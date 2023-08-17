
#from typing import Iterable

class ViewModel:
    def __init__(self, items):
        self._items = items
 
    @property
    def items(self):
        return self._items
    
    @property
    def done_items(self):
        done_items_list = [item for item in self._items if item['status'] == 'Done' ]
        return done_items_list
    
    @property
    def doin_items(self):
        doin_items_list = [item for item in self._items if item['status'] == 'Doin' ]
        return doin_items_list   
    
    @property
    def todo_items(self):
        todo_items_list = [item for item in self._items if item['status'] == 'Todo' ]
        return todo_items_list   