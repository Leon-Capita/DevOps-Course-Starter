from typing import Iterable
from todo_app.ItemClass import Item
from todo_app.debugger import writelog
from dotenv import load_dotenv, find_dotenv
import os

context = 'test_view_model.py'
doing = 'getting env vars'

file_path = find_dotenv('tests/.env.test')
load_dotenv(file_path, override=True)
TRELLO_TODO_ID = os.getenv('TRELLO_TODO_ID') 
TRELLO_DOIN_ID = os.getenv('TRELLO_DOIN_ID') 
TRELLO_DONE_ID = os.getenv('TRELLO_DONE_ID') 

def test_view_model_todo_property():
    context = 'test_view_model.py'
    doing = 'test_view_model_todo_property'
    #arrange
    test_items_list = [ 
        Item('someArbTestID1','ATodoTask',TRELLO_TODO_ID),
        Item('someArbTestID2','AnotherTodoTask','TodoID1'),
        Item('someArbTestID3','ADoinTask',TRELLO_DOIN_ID),
        Item('someArbTestID4','AnotherDoinTask','DoinID1'),
        Item('someArbTestID5','ADoneTask',TRELLO_DONE_ID),
        Item('someArbTestID6','AnotherDoneTask','DoneID1')
    ]   

    from todo_app.ViewModelClass import ViewModel
    # #act
    item_view_model = ViewModel(test_items_list).todo_items

    #assert
    # test1counter = 0
    # writelog(context, doing, 'SET test1counter', test1counter) 
    # for item in item_view_model:
    #     #writelog(context, doing, 'item', item) 
    #     #writelog(context, doing, 'TodoID1', 'TodoID1') 
    #     #writelog(context, doing, 'item.idList', item.idList) 
    #     if item.idList == 'TodoID1':
    #         test1counter+=1
    #     writelog(context, doing, 'INC test1counter', test1counter) 
    # assert test1counter == 1
    
    test2counter = 0
    for item in item_view_model:
        if item.idList == TRELLO_TODO_ID:
            test2counter+=1
    assert test2counter == 1

def test_view_model_doin_property():
    context = 'test_view_model.py'
    doing = 'test_view_model_doin_property'
    #arrange
    from todo_app.ViewModelClass import ViewModel
    test_items_list = [ 
        Item('someArbTestID1','ATodoTask',TRELLO_TODO_ID),
        Item('someArbTestID2','AnotherTodoTask','TodoID1'),
        Item('someArbTestID3','ADoinTask',TRELLO_DOIN_ID),
        Item('someArbTestID4','AnotherDoinTask','DoinID1'),
        Item('someArbTestID5','ADoneTask',TRELLO_DONE_ID),
        Item('someArbTestID6','AnotherDoneTask','DoneID1')
    ]   

    # #act
    item_view_model = ViewModel(test_items_list).doin_items
    
    # #assert
    # test1counter = 0
    # for item in item_view_model:
    #     writelog(context, doing, 'item', item) 
    #     if item.idList == 'DoinID1':
    #         test1counter+=1
    # assert test1counter == 1
    
    test2counter = 0
    for item in item_view_model:
        if item.idList == TRELLO_DOIN_ID:
            test2counter+=1
    assert test2counter == 1

def test_view_model_done_property():
    context = 'test_view_model.py'
    doing = 'test_view_model_doin_property'
    #arrange
    from todo_app.ViewModelClass import ViewModel
    test_items_list = [ 
        Item('someArbTestID1','ATodoTask',TRELLO_TODO_ID),
        Item('someArbTestID2','AnotherTodoTask','TodoID1'),
        Item('someArbTestID3','ADoinTask',TRELLO_DOIN_ID),
        Item('someArbTestID4','AnotherDoinTask','DoinID1'),
        Item('someArbTestID5','ADoneTask',TRELLO_DONE_ID),
        Item('someArbTestID6','AnotherDoneTask','DoneID1')
    ]   

    # #act
    item_view_model = ViewModel(test_items_list).done_items

    #assert
    # test1counter = 0
    # for item in item_view_model:
    #     writelog(context, doing, 'item', item) 
    #     if item.idList == 'DoneID1':
    #         test1counter+=1
    # assert test1counter == 1
    
    test2counter = 0
    for item in item_view_model:
        if item.idList == TRELLO_DONE_ID:
            test2counter+=1
    assert test2counter == 1