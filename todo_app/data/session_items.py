from flask import session#, request

_DEFAULT_ITEMS = [
   { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
   { 'id': 2, 'status': 'Started', 'title': 'Allow new items to be added' }
]
# class Todo_item:
#     def __init__(self, id, status, title ):
#         self.id = id
#         self.status = status #?boolean
#         self.title = title
#         #self.class or color = color
#     def __repr__(self):
#         return repr((self.id, self.status, self.title))
#     # def add_todo_item(self, id, status, title ):
#     #     todo_item_count +=1
#     #     _DEFAULT_ITEMS += id, status, title 
    
# # todo_item_count = 3
# _DEFAULT_ITEMS= [
#     Todo_item(1,'Not Started','List saved todo items'),
#     Todo_item(2,'Started','Allow new items to be added'),
#     Todo_item(3,'Not Started','Another to sort'),
# ]

def get_id(val):
    return val['id']

def get_status(val):
    return val['status']

def get_title(val):
    return val['title']

def get_items():
    """
    Fetches all saved items from the session.
    Returns:
        list: The list of saved items.
    """
    sorted_items = _DEFAULT_ITEMS.sort(key=get_status)
    #return session.get('items', _DEFAULT_ITEMS.copy())
    print(session)
    return session.get('items', sorted_items)

def get_item(id):
    """
    Fetches the saved item with the specified ID.
    Args:
        id: The ID of the item.
    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)

def add_item(title):
    """
    Adds a new item with the specified title to the session.
    Args:
        title: The title of the item.
    Returns:
        item: The saved item.
    """
    items = get_items()
    # Determine the ID for the item based on that of the previously added item
    id = items[-1]['id'] + 1 if items else 0
    item = { 'id': id, 'status': 'Not Started', 'title': title }
    #item = { 'id': id, 'title': title, 'status': 'Not Started' }
    # Add the item to the list
    items.append(item)
    session['items'] = items
    return item

def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.
    Args:
        item: The item to save.
    """
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]
    session['items'] = updated_items
    return item

def delete_item(id):
    """
    Deleted and existing item in the sessions.
    Args:
        item: The item to delete
    """
    existing_items = get_items()
    #items.remove[id]
    # for key, value in dict(existing_items).items():
    #     if value == id:
    #         del dict[key]
    #del items[id]
    #existing_items 
    #new_item_list = {k:v for k, v in existing_items.items() if v != id }
    new_item_list = [item for item in existing_items if item['id'] != id ]

    session['items'] = new_item_list
    #return item
    
