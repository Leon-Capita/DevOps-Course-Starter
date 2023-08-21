
#from typing import Iterable

class ViewModel:
    def __init__(self, items):
        self._items = items
 
    @property
    def items(self):
        return self._items
    
    # @property
    # def get_item_status(self, title):
    #     theitem = [item for item in self._items if item['title'] == title ]
    #     item_status = theitem['status']
    #     return item_status
    
    @property
    def done_items(self):
        #done_items_list = [item for item in self._items if item['status'] == 'Done' ]
        done_items_list = [item for item in self._items if item['idList'] == '64ae6f476f946f8c451a5cbb' ]
        return done_items_list
    
    @property
    def doin_items(self):
        #doin_items_list = [item for item in self._items if item['status'] == 'Doin' ]
        doin_items_list = [item for item in self._items if item['idList'] == '64ae6f476f946f8c451a5cba' ]
        return doin_items_list   
    
    @property
    def todo_items(self):
        #todo_items_list = [item for item in self._items if item['status'] == 'Todo' ]
        todo_items_list = [item for item in self._items if item['idList'] == '64ae6f476f946f8c451a5cb9' ]
        return todo_items_list   