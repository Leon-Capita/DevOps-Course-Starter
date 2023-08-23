from typing import Iterable
from todo_app.ItemClass import Item
from todo_app.debug import debug

# import sys
# sys.setrecursionlimit(5000)

def test_view_model_todo_property():
    context = 'test_view_model.py'
    doing = 'test_view_model_todo_property'
    #arrange
    from todo_app.ViewModelClass import ViewModel
    items = [ 
        Item('someArbTestID1','ATodoTask','64ae6f476f946f8c451a5cb9'),
        Item('someArbTestID2','AnotherTodoTask','TodoID1'),
        Item('someArbTestID3','ADoinTask','64ae6f476f946f8c451a5cba'),
        Item('someArbTestID4','AnotherDoinTask','DoinID1'),
        Item('someArbTestID5','ADoneTask','64ae6f476f946f8c451a5cbb'),
        Item('someArbTestID6','AnotherDoneTask','DoneID1')
    ]   
    debug(context, doing, 'items',items)

    # #act
    item_view_model = ViewModel(items).todo_items
    debug(context, doing, 'item_view_model', item_view_model) 

    #assert
    test1counter = 0
    for item in item_view_model:
        debug(context, doing, 'item', item) 
        if item.idList == 'TodoID1':
            test1counter+=1
    assert test1counter == 0
    
    test2counter = 0
    for item in item_view_model:
        debug(context, doing, 'item', item) 
        if item.idList == '64ae6f476f946f8c451a5cb9':
            test2counter+=1
    assert test2counter == 1

def test_view_model_doin_property():
    context = 'test_view_model.py'
    doing = 'test_view_model_doin_property'
    #arrange
    from todo_app.ViewModelClass import ViewModel
    items = [ 
        Item('someArbTestID1','ATodoTask','64ae6f476f946f8c451a5cb9'),
        Item('someArbTestID2','AnotherTodoTask','TodoID1'),
        Item('someArbTestID3','ADoinTask','64ae6f476f946f8c451a5cba'),
        Item('someArbTestID4','AnotherDoinTask','DoinID1'),
        Item('someArbTestID5','ADoneTask','64ae6f476f946f8c451a5cbb'),
        Item('someArbTestID6','AnotherDoneTask','DoneID1')
    ]   
    debug(context, doing, 'items',items)

    # #act
    item_view_model = ViewModel(items).doin_items
    debug(context, doing, 'item_view_model', item_view_model) 

    #assert
    test1counter = 0
    for item in item_view_model:
        debug(context, doing, 'item', item) 
        if item.idList == 'DoinID1':
            test1counter+=1
    assert test1counter == 0
    
    test2counter = 0
    for item in item_view_model:
        debug(context, doing, 'item', item) 
        if item.idList == '64ae6f476f946f8c451a5cba':
            test2counter+=1
    assert test2counter == 1

def test_view_model_done_property():
    context = 'test_view_model.py'
    doing = 'test_view_model_doin_property'
    #arrange
    from todo_app.ViewModelClass import ViewModel
    items = [ 
        Item('someArbTestID1','ATodoTask','64ae6f476f946f8c451a5cb9'),
        Item('someArbTestID2','AnotherTodoTask','TodoID1'),
        Item('someArbTestID3','ADoinTask','64ae6f476f946f8c451a5cba'),
        Item('someArbTestID4','AnotherDoinTask','DoinID1'),
        Item('someArbTestID5','ADoneTask','64ae6f476f946f8c451a5cbb'),
        Item('someArbTestID6','AnotherDoneTask','DoneID1')
    ]   
    debug(context, doing, 'items',items)

    # #act
    item_view_model = ViewModel(items).done_items
    debug(context, doing, 'item_view_model', item_view_model) 

    #assert
    test1counter = 0
    for item in item_view_model:
        debug(context, doing, 'item', item) 
        if item.idList == 'DoneID1':
            test1counter+=1
    assert test1counter == 0
    
    test2counter = 0
    for item in item_view_model:
        debug(context, doing, 'item', item) 
        if item.idList == '64ae6f476f946f8c451a5cbb':
            test2counter+=1
    assert test2counter == 1