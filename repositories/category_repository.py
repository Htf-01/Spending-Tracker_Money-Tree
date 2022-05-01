# Imports
from db.run_sql import run_sql
from models.category import Category

# CREATE
###############################################################
def save(category):
    sql = "INSERT INTO categories(name,activated) VALUES ( %s,%s) RETURNING id"
    values = [category.name, category.activated]
    results = run_sql( sql, values )
    category.id = results[0]['id']
    return category.id

# READ
###############################################################
def select_all():
    categories = []

    sql = "SELECT * FROM categories"
    results = run_sql(sql)

    for row in results:
        category = Category(row['name'], row['activated'], row['id'])
        categories.append(category)
    return categories

def select_all_activated():
    categories = []

    sql = "SELECT * FROM categories where activated = True order by name"
    results = run_sql(sql)

    for row in results:
        category = Category(row['name'], row['activated'], row['id'])
        categories.append(category)
    return categories




def select(id):
    category = None
    sql = "SELECT * FROM categories WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        category = Category(result['name'], result['activated'], result['id'])
    return category

def select_by_name(name):

    sql = "Select * from categories where name = %s"
    values = [name]
    run = run_sql(sql, values)
    
    if run:
        result = run[0]
        category = Category(result['name'], result['activated'], result['id'])
        return category
    else:
        return False

# UPDATE
###############################################################
def update(category):
    sql = "UPDATE categories SET (name,activated,filtered) = ( %s,%s) WHERE id = %s"
    values = [category.name, category.activated, category.id]
    run_sql(sql, values)
    
def update_activated(category):
    sql = "UPDATE categories SET activated = (%s) WHERE id = %s"
    category.flip_activated()
    values = [category.activated, category.id]
    run_sql(sql, values)


# DELETE
###############################################################
def delete_all():
    sql = "DELETE FROM categories"
    run_sql(sql)