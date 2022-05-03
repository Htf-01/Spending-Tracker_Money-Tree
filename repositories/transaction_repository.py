# Imports
from db.run_sql import run_sql
from models.transaction import Transaction

import repositories.category_repository as category_repository
import repositories.merchant_repository as merchant_repository


# CREATE
###############################################################
def save(transaction):
    sql = "INSERT INTO transactions(transaction_date,merchant_id,category_id,amount) VALUES ( %s,%s,%s,%s) RETURNING id"
    values = [transaction.date, transaction.merchant.id, transaction.category.id, transaction.amount]
    results = run_sql( sql, values )
    transaction.id = results[0]['id']

# READ
###############################################################
def select_all(values,sort):
    transactions = []
    if sort == 'transaction_date':
        sql = '''SELECT t.* 
                FROM transactions as t
                JOIN categories as c
                ON t.category_id = c.id
                JOIN merchants as m
                ON t.merchant_id = m.id
                WHERE extract (month from transaction_date) = %s
                AND EXTRACT(YEAR FROM transaction_date) = %s
                AND c.activated = True
                AND m.activated = True
                ORDER BY transaction_date DESC'''
            
    elif sort == 'merchant_id':
        sql = '''SELECT t.* 
                FROM transactions as t
                JOIN categories as c
                ON t.category_id = c.id
                JOIN merchants as m
                ON t.merchant_id = m.id
                WHERE extract (month from transaction_date) = %s
                AND EXTRACT(YEAR FROM transaction_date) = %s
                AND c.activated = True
                AND m.activated = True
                ORDER BY m.name'''

    elif sort == 'category_id':
        sql = '''SELECT t.* 
                FROM transactions as t
                JOIN categories as c
                ON t.category_id = c.id
                JOIN merchants as m
                ON t.merchant_id = m.id
                WHERE extract (month from transaction_date) = %s
                AND EXTRACT(YEAR FROM transaction_date) = %s
                AND c.activated = True
                AND m.activated = True
                ORDER BY c.name'''
    else: 
        sort == 'amount'
        sql = '''SELECT t.* 
                FROM transactions as t
                JOIN categories as c
                ON t.category_id = c.id
                JOIN merchants as m
                ON t.merchant_id = m.id
                WHERE extract (month from transaction_date) = %s
                AND EXTRACT(YEAR FROM transaction_date) = %s
                AND c.activated = True
                AND m.activated = True
                ORDER BY amount desc'''

    results = run_sql(sql, values)
    
    sql_total = '''SELECT sum(t.amount)
                FROM transactions as t
                JOIN categories as c
                ON t.category_id = c.id
                JOIN merchants as m
                ON t.merchant_id = m.id
                WHERE extract (month from transaction_date) = %s
                AND EXTRACT(YEAR FROM transaction_date) = %s
                AND c.activated = True
                AND m.activated = True'''
    
    total = run_sql(sql_total, values)[0]

    for row in results:
        merchant = merchant_repository.select(row['merchant_id'])
        category = category_repository.select(row['category_id'])
        transaction = Transaction(row['transaction_date'], merchant,row['amount'],category, row['id'])
        transactions.append(transaction)
    return transactions,total

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

# UPDATE
###############################################################
def update(transaction):
    sql = "UPDATE transactions SET (transaction_date,merchant_id,category_id,amount) = ( %s,%s,%s,%s ) WHERE id = %s"
    values = [transaction.date, transaction.merchant.id, transaction.category.id, transaction.amount, transaction.id]
    run_sql(sql, values)
    
# DELETE
###############################################################
def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)
    