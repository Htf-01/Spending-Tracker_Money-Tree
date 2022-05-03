from datetime import datetime, date
from dateutil.relativedelta import relativedelta


class Transaction ():
    
    def __init__(self, date, merchant, amount, category = None, id = None):
        self.date = Transaction.string_to_date(date)                  # date picker format = YYYY-MM-DD
        self.merchant = merchant
        self.amount = amount
        self.category = category
        self.id = id
        
    def currency_format(self):
        return f'£{(self.amount/100):.2f}'
    
    def date_format(self):
        return f'{self.date.day:02d}-{self.date.month:02d}-{self.date.year}'
    
    def string_to_date(date):
        if isinstance(date,str):
            return datetime.date(datetime.strptime(date,'%Y-%m-%d'))
        else:
            return date
        
        # Session functions
    def session_today():
       return date.today()                
    
    def session_date_display(session):
        month = datetime.strptime(str((session['current']['month'])), "%m").strftime("%b")
        year = datetime.strptime(str((session['current']['year'])), "%Y").strftime("%y")
        return f'{month} {year}'
    
    def session_increment(session):
        date = f'{session["current"]["month"]}-{(session["current"]["year"])}'
        new_date = (datetime.strptime(date, "%m-%Y")) + relativedelta(months=+1)
        session['current']['month']=new_date.month
        session['current']['year']=new_date.year
        session.modified = True
    
    def session_decrement(session):
        date = f'{session["current"]["month"]}-{(session["current"]["year"])}'
        new_date = (datetime.strptime(date, "%m-%Y")) + relativedelta(months=-1)
        session['current']['month']=new_date.month
        session['current']['year']=new_date.year
        session.modified = True
        
    def session_current(session): 
        session['current']['month']= session['date']['month']
        session['current']['year']=session['date']['year']
        session.modified = True
        
    def session_select(session, date_string):
        new_date = (datetime.strptime(date_string, '%Y-%m'))
        session['current']['month']= new_date.month
        session['current']['year']=new_date.year
        session.modified = True
        
    def session_sql_format(session):
        month = session['current']['month']
        year = session['current']['year']
        return [month, year]
    
    # Sort
    
    def session_edit_sort(session,sort):
        session['sort']['sort'] = sort
        session.modified = True
        
    def session_return_sort(session):
        return session['sort']['sort']
    
        

        
    

    
    
        
