from datetime import datetime
from time import strftime

class Transaction ():
    
    def __init__(self, date, merchant, amount, category = None, budget_id = None, id = None):
        self.date = Transaction.string_to_date(date)                  # date picker format = YYYY-MM-DD
        self.merchant = merchant
        self.amount = amount
        self.category = category
        self.id = id
        self.budget_id = budget_id
        
        
    def currency_format(self):
        return f'£{(self.amount/100):.2f}'
    
    def date_format(self):
        return f'{self.date.day}-{self.date.month}-{self.date.year}'
    
    def string_to_date(date):
        if isinstance(date,str):
            return datetime.date(datetime.strptime(date,'%Y-%m-%d'))
        else:
            return date
    
    
        
