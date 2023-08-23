from todo_app.ItemClass import Item
from todo_app.debug import debug

class ViewModel:
    def __init__(self, todo_items: list[Item], doin_items: list[Item], done_items: list[Item]):
        self._items: list[Item] = todo_items + doin_items + done_items

    # @property
    # def items(self):
    #     return self._items
    
    # def __getitem__(self, key): # this allows getting an element (overrided method)
    #     return self._items[key]
    
    @property
    def todo_items(self) -> list[Item]:
        todo_items_list: list[Item] = []   
        for item in self._items:
            if item['idList'] == '64ae6f476f946f8c451a5cb9':
                todo_items_list.append(item)
        return todo_items_list

    @property
    def doin_items(self) -> list[Item]:
        doin_items_list: list[Item] = []   
        for item in self._items:
            if item['idList'] == '64ae6f476f946f8c451a5cba':
                doin_items_list.append(item)
        return doin_items_list

    @property
    def done_items(self) -> list[Item]:
        done_items_list: list[Item] = []   
        for item in self._items:
            if item['idList'] == '64ae6f476f946f8c451a5cbb':
                done_items_list.append(item)
        return done_items_list