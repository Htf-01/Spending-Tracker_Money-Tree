from datetime import datetime


class Transaction ():
    
    
    # default sort by value for the select_all function.
    # Can be changed by html forms
    sort = 'transaction_date'
    
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
        return f'{self.date.day:02d}-{self.date.month:02d}-{self.date.year}'
    
    def string_to_date(date):
        if isinstance(date,str):
            return datetime.date(datetime.strptime(date,'%Y-%m-%d'))
        else:
            return date
    
    
        
