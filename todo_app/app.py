from flask import Flask, request, render_template, redirect
from todo_app.ViewModelClass import ViewModel
from todo_app.flask_config import Config
#from todo_app.data.session_items import get_items,delete_item, get_item, add_item, save_item, get_item_id_by_title, get_item_by_title#, get_item_status
from todo_app.data.trello import get_trello_cards, add_trello_card, del_trello_card, get_trello_card_id_by_name, get_trello_card_by_name, upd_trello_card
from todo_app.ItemClass import Item
from todo_app.debug import debug

###Move debug logging out and simplify
###Would like an undo feature - keep details of previous action and be able to click undo 
###List of credits to tech used, eg flask, trello etc

def test_func():
    pass

def create_app(debug=True):
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/', methods = ["GET"])
    def index():
        context = 'app.py index route'
        doing = 'trello_cards'
        #items = get_items()
        #items = get_trello_cards()
        trello_items = get_trello_cards()
        #debug(context, doing, 'trello_items',trello_items)
        items = []
        doing = 'building items'
        #debug(context, doing, 'items',items)
        for item in trello_items:
            #debug(context, doing, 'item',item)
            #items.append(Item(id=item_id, name=item_name, status=item_list))
            items.append(Item(item['id'], item['name'], item['idList']))
            #debug(context, doing, 'items',items)
        item_view_model = ViewModel(items)
        #item_view_model = items
        return render_template('index.html', view_model=item_view_model)
        # return render_template('index.html', items_list = items)

    @app.route('/add-item', methods = ["POST"])
    def add_todo_item():
        item_title = request.form.get('title')
        #add_item(item_title)
        add_trello_card(item_title)
        context = 'app.py add-item route'
        doing = 'add_trello_card'
        debug(context, doing, 'item_title',item_title)
        return redirect('/')

    @app.route('/del-item', methods = ["POST"])
    def del_todo_item():
        exis_item_title = request.form.get("selected_item")
        #id = get_item_id_by_title(exis_item_title)
        id = get_trello_card_id_by_name(exis_item_title)
        #delete_item(id)
        del_trello_card(id)
        context = 'app.py del-item route'
        doing = 'del_trello_card'
        debug(context, doing, 'id',id)
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
        
        context = 'app.py upd-item route'
        doing = 'upd_trello_card'
        debug(context, doing, 'item',item)
        #save_item(item)
        upd_trello_card(item_id, item_title, item_status)
        return redirect('/')

    return app
