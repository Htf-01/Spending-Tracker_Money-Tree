from datetime import date, datetime


class Budget ():
   
    current_budget = None
    
    def __init__(self, date, amount=0, id=None):
        
        self.date = date
        self.amount = amount
        self.id = id
    
    def convert_date(date):
        return datetime.date(datetime.strptime(date,'%Y-%m'))
    
    def today ():
        return date.today()
    
    def date_format_display (budget_date):
        return date.strftime(budget_date, '%b %y')
    
    def date_format_picker (budget_date):
        return date.strftime(budget_date, '%Y-%m')
    
    def set_current_budget(id):
        Budget.current_budget = id
    
        
        

        