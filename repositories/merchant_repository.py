# Imports
from db.run_sql import run_sql
from models.merchant import Merchant

# CREATE
###############################################################
def save(merchant):
    sql = "INSERT INTO merchants(name,activated,filtered) VALUES ( %s,%s,%s ) RETURNING id"
    values = [merchant.name, merchant.activated, merchant.filtered]
    results = run_sql( sql, values )
    merchant.id = results[0]['id']
    return merchant.id

# READ
###############################################################
def select_all():
    merchants = []

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)

    for row in results:
        merchant = Merchant(row['name'], row['activated'], row['filtered'], row['id'])
        merchants.append(merchant)
    return merchants

def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result['name'], result['activated'], result['filtered'], result['id'])
    return merchant

def select_by_name(name):

    sql = "Select * from merchants where name = %s"
    values = [name]
    run = run_sql(sql, values)
    
    if run:
        result = run[0]
        merchant = Merchant(result['name'], result['activated'], result['filtered'], result['id'])
        return merchant
    else:
        return False
    
    
# UPDATE
###############################################################
def update(merchant):
    sql = "UPDATE merchants SET (name,activated,filtered) = ( %s,%s,%s ) WHERE id = %s"
    values = [merchant.name, merchant.activated, merchant.filtered, merchant.id]
    run_sql(sql, values)
    
def update_activated(merchant):
    sql = "UPDATE merchants SET activated = (%s) WHERE id = %s"
    merchant.flip_activated()
    values = [merchant.activated, merchant.id]
    run_sql(sql, values)

def update_filtered(merchant):
    sql = "UPDATE merchants SET filtered = (%s) WHERE id = %s"
    merchant.flip_filtered()
    values = [merchant.filtered, merchant.id]
    run_sql(sql, values)

# DELETE
###############################################################
def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)