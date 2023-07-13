from todo_app.data.session_items import add_item, get_items, get_item, save_item, delete_item
from flask import Flask, redirect, render_template, request
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    items = get_items()
    #unsorteditems = get_items()
    #items = (sorted(unsorteditems.status(), key=lambda item:item[1]))
    return render_template('index.html', items_list = items)

@app.route('/add-item', methods = ["POST"])
#def add_item(self):
#def add_item():
#@staticmethod
def add_todo_item():
    item_title = request.form.get('title')
    add_item(item_title)
    return redirect('/')

@app.route("/get-item", methods = ["POST"])
def get_todo_item():
    pass

@app.route('/upd-item', methods = ["POST"])
def upd_todo_item():
    item_id = int(request.form.get('upd_id'))
    if(item_id>0):
        print(item_id)
        #item_status = request.form.get('status')
        item_status = request.form.get("options")
        item_title = request.form.get('title')
        item = { 'id': item_id, 'status': item_status, 'title': item_title }
        save_item(item)
    return redirect('/')

# @app.route("/del-item", methods = ["POST"])
# def del_todo_item():
#     items = get_items()
#     return render_template('del-item.html', items_list = items) #, items_list = items
#@app.route("/del-item", methods = ["POST"])
#def del_todo_item():
    #item_id = int(request.form.get('del_id'))
    #delete_item(item_id)
    #return redirect('/')