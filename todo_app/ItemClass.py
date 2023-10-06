class Item:
    def __init__(self, id, name, idList):
        self.id = id
        self.name = name
        self.idList = idList
    
    def __repr__(self): # How the cards appear in your list
        return str(self.id) + str(self.name) + str(self.idList)

