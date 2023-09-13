
#from typing import Iterable

from typing import Any
from todo_app.debugger import writelog

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

    # def __getattribute__(self, __name: str) -> Any:
    #     pass

    def __getitem__(self, key): # this allows getting an element (overrided method)
        return self._items[key]
    
    @property
    def done_items(self):
        context = 'ViewModelClass.py done_items'
        doing = 'done_items'
        #done_items_list = [item for item in self._items if item['status'] == 'Done' ]
        #done_items_list = [item for item in self._items if item['idList'] == '64ae6f476f946f8c451a5cbb' ]
        done_items_list = [item for item in self._items if item.idList == '64ae6f476f946f8c451a5cbb' ]
        return done_items_list
    
    @property
    def doin_items(self):
        context = 'ViewModelClass.py doin_items'
        doing = 'doin_items'
        #doin_items_list = [item for item in self._items if item['status'] == 'Doin' ]
        #doin_items_list = [item for item in self._items if item['idList'] == '64ae6f476f946f8c451a5cba' ]
        doin_items_list = [item for item in self._items if item.idList == '64ae6f476f946f8c451a5cba' ]
        return doin_items_list   
    
    @property
    def todo_items(self):
        context = 'ViewModelClass.py todo_items'
        doing = 'todo_items'
        #for item in self._items:
            #idList = item['idList']
            # print(f'in ViewModel.todo_items: item[`idList`] {idList}')
            #writelog(context, doing, 'self._items',self._items)    
            #writelog(context, doing, 'item', item) 
            #writelog(context, doing, 'item[`idList`]', item['idList']) 
            #writelog(context, doing, 'item.idList', item.idList) 
        #todo_items_list = [item for item in self._items if item['status'] == 'Todo' ]
        #writelog(context, doing, 'self._items',self._items)
        todo_items_list = [item for item in self._items if item.idList == '64ae6f476f946f8c451a5cb9' ]
        return todo_items_list   
    


    