# Imports
from db.run_sql import run_sql
from models.budget import Budget

# CREATE
###############################################################


# READ
###############################################################


def select_budget(dates):
    budget_id = None
    sql = '''SELECT id FROM budgets 
    WHERE month(date) = %s AND YEAR(date) = %s'''
    values = [dates[0],dates[1]]
    result = run_sql(sql, values)[0]

    if result is not None:
        budget_id = result['id']
    return budget_id



# UPDATE
###############################################################

    
# DELETE
###############################################################
