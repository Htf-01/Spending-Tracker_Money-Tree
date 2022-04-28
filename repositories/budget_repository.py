# Imports
from db.run_sql import run_sql
from models.budget import Budget

# CREATE
###############################################################
def save(budget):
    sql = "INSERT INTO budgets (date) VALUE ( %s) RETURNING id"
    values = [budget.date]
    results = run_sql( sql, values )
    category.id = results[0]['id']

# READ
###############################################################
def select_all():
    categories = []

    sql = "SELECT * FROM categories"
    results = run_sql(sql)

    for row in results:
        category = Category(row['name'], row['activated'], row['filtered'], row['id'])
        categories.append(category)
    return categories

def select(id):
    category = None
    sql = "SELECT * FROM categories WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        category = Category(result['name'], result['activated'], result['filtered'], result['id'])
    return category


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
def update(category):
    sql = "UPDATE categories SET (name,activated,filtered) = ( %s,%s,%s ) WHERE id = %s"
    values = [category.name, category.activated, category.filtered, category.id]
    run_sql(sql, values)
    
# DELETE
###############################################################
