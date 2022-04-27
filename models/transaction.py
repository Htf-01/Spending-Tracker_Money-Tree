class Transaction ():
    
    def __init__(self, date, merchant, amount, category = None, id = None):
        self.date = date
        self.merchant = merchant
        self.amount = amount
        self.category = category
        self.id = id