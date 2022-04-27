class Merchant ():
    
    def __init__(self, name, activated = True, filtered = True, id= None):
        self.name = name
        self.activated = activated
        self.filter = filtered
        self.id = id
    