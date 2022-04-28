from datetime import datetime

class Transaction ():
    
    def __init__(self, date, merchant, amount, category = None, id = None):
        self.date = date                  # date picker format = YYYY-MM-DD
        self.merchant = merchant
        self.amount = amount
        self.category = category
        self.id = id
        self.budget_selector = self.date_conversion()
        
        
    def amount_to_string(self):
        return f'£{(self.amount/100):.2f}'
    
    def date_conversion(self):
        conversion = datetime.strptime(self.date,'%Y-%m-%d')
        return [conversion.strftime('%m'),conversion.strftime('%Y')]
    
    
        
