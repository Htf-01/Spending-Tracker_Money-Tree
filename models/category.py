class Category ():
    
    def __init__(self, name, activated = True, id = None):
        self.name = name
        self.activated = activated
        self.id = id
    
    def flip_activated (self):
        if self.activated:
            self.activated = False
        else:
            self.activated = True