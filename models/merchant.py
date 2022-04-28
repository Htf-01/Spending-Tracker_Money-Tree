class Merchant ():
    
    def __init__(self, name, activated = True, filtered = True, id= None):
        self.name = name
        self.activated = activated
        self.filtered = filtered
        self.id = id
        
    def flip_activated (self):
        if self.activated:
            self.activated = False
        else:
            self.activated = True
            
    def flip_filtered (self):
        if self.filtered:
            self.filtered = False
        else:
            self.filtered = True