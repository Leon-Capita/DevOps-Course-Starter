class Item:
    #def __init__(self, id, name, status = 'To Do'):
    def __init__(self, id, name, idList):
        self.id = id
        self.name = name
        self.idList = idList

    # @classmethod
    # def from_trello_card(cls, card, list):
    #     return cls(card['id'], card['name'], list['idList'])
    
    # def __getattr__():
    #     pass

    # def get_item_id(self):
    #     return self.id
    
    # def get_item_name(self):
    #     return self.name
    
    # def get_item_status(self):
    #     return self.idList
