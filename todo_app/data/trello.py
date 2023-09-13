from todo_app.data.config import TRELLO_BOARD_ID, TRELLO_APIKEY, TRELLO_TOKEN, TRELLO_TODO_ID, TRELLO_DOIN_ID, TRELLO_DONE_ID
import requests
import json
debuglevel=2

def get_trello_cards():
    if debuglevel>1:print('=====================get_trello_lists')
    url = "https://api.trello.com/1/boards/"+TRELLO_BOARD_ID+"/lists" #fields=all
    #url = "https://api.trello.com/1/boards/"+TRELLO_BOARD_ID+"/lists?fields=id,name,shortUrl" #fields=all
    if debuglevel>1:print (url)
    headers = { "Accept": "application/json" }
    query = { 'key': TRELLO_APIKEY,'token': TRELLO_TOKEN, "cards":"open", "card_fields":"name,idList" }
    response = requests.request("GET", url, headers=headers, params=query )
    if debuglevel>1:print(response.json())
    resp = response.json()

    cards = []
    for list in resp:
        for card in list['cards']:
            if debuglevel>0:print(f"card {card}")
            #card['listname']=list['name']
            cards.append(card)
    return cards

def add_trello_card(name):
    url = "https://api.trello.com/1/cards"
    headers = { "Accept": "application/json" }
    query = { 'idList': TRELLO_TODO_ID, 'key': TRELLO_APIKEY, 'token': TRELLO_TOKEN, "name":name }
    response = requests.request("POST", url, headers=headers, params=query )
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

def del_trello_card(id):
    url = "https://api.trello.com/1/cards/"+id
    query = { 'key': TRELLO_APIKEY, 'token': TRELLO_TOKEN }
    response = requests.request("DELETE", url, params=query )
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

def upd_trello_card(id, name, idList):
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


