from flask import Flask, request, render_template, redirect
from todo_app.ViewModelClass import ViewModel
from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, get_item, add_item, save_item#, get_item_by_title
from logging.config import logging

debug=2
if debug>0: print (f'DEBUG ON - level {debug}')
app = Flask(__name__)
app.config.from_object(Config())
logging.basicConfig(filename='todo.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s : %(message)s')

@app.route('/')
def index():
    items = get_items()
    item_view_model = ViewModel(items)
    return render_template('index.html', view_model=item_view_model)
    # return render_template('index.html', items_list = items)

@app.route('/add-item', methods = ["POST"])
def add_todo_item():
    item_title = request.form.get('title')
    add_item(item_title)
    return redirect('/')

# @app.route("/get-item-title", methods = ["POST"])
# def get_item_title():
#     item_title = request.form.get('dropdownMenuReference')
#     return redirect('/')



@app.route('/upd-item', methods = ["POST"])
def upd_todo_item():
    items = get_items()
    if debug>0: print (f'items {items}')
    item_status = request.form.get("options")
    if debug>0: print (f'item_status {item_status}')
    item_title = request.form.get('upd_title')
    if debug>0: print (f'upd_title {upd_title}')

    theitem = (item for item in items if item['title'] == item_title)
    if debug>0: print (f'theitem {theitem}')
    item_id = theitem['id']
    if debug>0: print (f'item_id {item_id}')

    item = { 'id': item_id, 'status': item_status, 'title': item_title }
    if debug>0: print (f'item {item}')
    save_item(item)
    return redirect('/')

