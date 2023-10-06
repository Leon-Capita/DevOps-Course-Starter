import requests, json, os
from todo_app.debugger import writelog
from dotenv import load_dotenv, find_dotenv

def get_trello_cards():
    TRELLO_BOARD_ID = os.getenv('TRELLO_BOARD_ID')
    TRELLO_APIKEY = os.getenv('TRELLO_APIKEY')
    TRELLO_TOKEN = os.getenv('TRELLO_TOKEN') 
    url = ("https://api.trello.com/1/boards/"+TRELLO_BOARD_ID+"/lists") #fields=all
    #url = "https://api.trello.com/1/boards/"+TRELLO_BOARD_ID+"/lists?fields=id,name,shortUrl" #fields=all
    headers = { "Accept": "application/json" }
    query = { 'key': TRELLO_APIKEY,'token': TRELLO_TOKEN, "cards":"open", "card_fields":"name,idList" }
    response = requests.request("GET", url, headers=headers, params=query )
    resp = response.json()

    cards = []
    for list in resp:
        for card in list['cards']:
            #card['listname']=list['name']
            cards.append(card)
    return cards

def add_trello_card(name):
    TRELLO_APIKEY = os.getenv('TRELLO_APIKEY')
    TRELLO_TOKEN = os.getenv('TRELLO_TOKEN') 
    TRELLO_TODO_ID = os.getenv('TRELLO_TODO_ID')  
    url = "https://api.trello.com/1/cards"
    headers = { "Accept": "application/json" }
    query = { 'idList': TRELLO_TODO_ID, 'key': TRELLO_APIKEY, 'token': TRELLO_TOKEN, "name":name }
    response = requests.request("POST", url, headers=headers, params=query )
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

def del_trello_card(id):
    TRELLO_APIKEY = os.getenv('TRELLO_APIKEY')
    TRELLO_TOKEN = os.getenv('TRELLO_TOKEN') 
    url = "https://api.trello.com/1/cards/"+id
    query = { 'key': TRELLO_APIKEY, 'token': TRELLO_TOKEN }
    response = requests.request("DELETE", url, params=query )
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

def upd_trello_card(id, name, idList):
    TRELLO_APIKEY = os.getenv('TRELLO_APIKEY')
    TRELLO_TOKEN = os.getenv('TRELLO_TOKEN') 
    url = "https://api.trello.com/1/cards/"+id
    headers = { "Accept": "application/json" }
    query = { 'key': TRELLO_APIKEY, 'token': TRELLO_TOKEN, "name":name, "idList":idList }
    response = requests.request( "PUT", url, headers=headers, params=query)

def get_trello_card_id_by_name(name):
    cards=[]
    cards = get_trello_cards()
    for card in cards:
        if card['name'] == name:
            id = card['id']
    return id

def get_trello_card_by_name(name):
    cards=[]
    cards = get_trello_cards()
    for card in cards:
        if card['name'] == name:
            card = card
    return card


