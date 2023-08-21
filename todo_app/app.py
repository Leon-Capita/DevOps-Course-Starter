from flask import Flask, request, render_template, redirect
from todo_app.ViewModelClass import ViewModel
from todo_app.flask_config import Config
from todo_app.data.session_items import get_items,delete_item, get_item, add_item, save_item, get_item_id_by_title, get_item_by_title#, get_item_status
from todo_app.data.trello import get_trello_cards, add_trello_card, del_trello_card, get_trello_card_id_by_name, get_trello_card_by_name, upd_trello_card
#from logging.config import logging
import logging 
###Would like an undo feature - keep details of previous action and be able to click undo 

debug=2
if debug>0: print (f'DEBUG ON - level {debug}')
logging.info(f'DEBUG ON - level {debug}')
app = Flask(__name__)
app.config.from_object(Config())
logging.basicConfig(filename='/c/temp/devops/projex/DevOps-Course-Starter2/todo.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s : %(message)s')

@app.route('/', methods = ["GET"])
def index():
    #items = get_items()
    items = get_trello_cards()
    item_view_model = ViewModel(items)
    logging.info(f'item_view_model {item_view_model}')
    return render_template('index.html', view_model=item_view_model)
    # return render_template('index.html', items_list = items)

@app.route('/add-item', methods = ["POST"])
def add_todo_item():
    item_title = request.form.get('title')
    #add_item(item_title)
    add_trello_card(item_title)
    #if debug>0: print (f'item_title {item_title}') 
    logging.info(f'item_title {item_title}')
    return redirect('/')

@app.route('/del-item', methods = ["POST"])
def del_todo_item():
    exis_item_title = request.form.get("selected_item")
    #id = get_item_id_by_title(exis_item_title)
    id = get_trello_card_id_by_name(exis_item_title)
    #delete_item(id)
    del_trello_card(id)
    if debug>0: print (f'id {id}')
    logging.info(f'id {id}')
    return redirect('/')

@app.route('/upd-item', methods = ["POST"])
def upd_todo_item():
    exis_item_title = request.form.get("selected_item")
    #exis_item = get_item_by_title(exis_item_title)
    exis_item = get_trello_card_by_name(exis_item_title) 
    #exis_item_status = exis_item['status']
    exis_item_status = exis_item['idList']

    item_status = request.form.get("status")
    item_title = request.form.get("upd_title")
    #item_id = get_item_id_by_title(exis_item_title)
    item_id = get_trello_card_id_by_name(exis_item_title)
    if item_title == '':
        #item = { 'id': item_id, 'status': item_status, 'title': exis_item_title }
        item = { 'id': item_id, 'idList': item_status, 'name': exis_item_title }
    else:
        #item = { 'id': item_id, 'status': item_status, 'title': item_title }
        item = { 'id': item_id, 'idList': item_status, 'name': item_title }
    
    if debug>0: print (f'item {item}')
    logging.info(f'item {item}')
    #save_item(item)
    upd_trello_card(item_id, item_title, item_status)
    return redirect('/')
