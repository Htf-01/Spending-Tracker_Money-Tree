# Imports
from db.run_sql import run_sql
from models.transaction import Transaction

import repositories.category_repository as category_repository
import repositories.merchant_repository as merchant_repository

# CREATE
###############################################################
def save(transaction):
    sql = "INSERT INTO transactions(transaction_date,merchant_id,category_id,amount,budget_id) VALUES ( %s,%s,%s,%s,%s) RETURNING id"
    budget_id = select_budget(transaction.budget_selector)
    values = [transaction.date, transaction.merchant.id, transaction.category.id, transaction.amount, budget_id]
    results = run_sql( sql, values )
    transaction.id = results[0]['id']

# READ
###############################################################
def select_all():
    transactions = []

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        merchant = merchant_repository.select(row['merchant_id'])
        category = category_repository.select(row['category_id'])
        transaction = Transaction(row['transaction_date'], merchant, row['amount'], category, row['id'])
        transactions.append(transaction)
    return transactions

def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = merchant_repository.select(result['merchant_id'])
        category = category_repository.select(result['category_id'])
        transaction = Transaction(result['transaction_date'], merchant, result['amount'],category, id)
    return transaction

def select_budget(dates):
    budget_id = None
    sql = '''SELECT id FROM budgets 
    WHERE Extract(month FROM budget_date) = %s AND
    extract(YEAR FROM budget_date) = %s'''

    values = [(dates[0]),(dates[1])]
    result = run_sql(sql,values)[0]
    
    if result is not None:
        budget_id = result['id']
    return budget_id

# UPDATE
###############################################################
def update(transaction):
    sql = "UPDATE transactions SET (transaction_date,merchant_id,category_id,amount) = ( %s,%s,%s,%s ) WHERE id = %s"
    values = [transaction.date, transaction.merchant.id, transaction.category.id, transaction.amount, transaction.id]
    run_sql(sql, values)
    


# DELETE
###############################################################

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)
    