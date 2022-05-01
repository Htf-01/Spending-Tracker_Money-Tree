# Imports
from db.run_sql import run_sql
from models.budget import Budget

# CREATE
###############################################################


# READ
###############################################################

def select_budget(date):
    budget_id = None
    sql = '''SELECT id FROM budgets 
    WHERE Extract(month FROM budget_date) = %s AND
    extract(YEAR FROM budget_date) = %s'''

    values = [date.month,date.year]
    result = run_sql(sql,values)[0]
    
    if result is not None:
        budget_id = result['id']
    return budget_id

def select_date(id):
    date = None
    sql = "SELECT * FROM budgets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
  
    if result is not None:
        date = result['budget_date']
    return date





# UPDATE
###############################################################

    
# DELETE
###############################################################



def get_current_budget():
    if Budget.current_budget == None:
        Budget.current_budget = select_budget(Budget.today())
        return Budget.current_budget
    else:
        return Budget.current_budget
