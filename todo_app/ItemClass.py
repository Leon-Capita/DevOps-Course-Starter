class Item:
    #def __init__(self, id, name, status = 'To Do'):
    def __init__(self, id, name, idList):
        self.id = id
        self.name = name
        self.idList = idList
    
    def __repr__(self): # How the cards appear in your list
        #return 'id: ' + str(self.id) +' name: '+ str(self.name) +' idList:'+ str(self.idList)
        return str(self.id) + str(self.name) + str(self.idList)
        #return str(self.id, self.name, self.idList)
        #return str(self)
    
    # def __repr__(self): # How the cards appear in your list
        # return str(self.figure) + str(self.colour)

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
