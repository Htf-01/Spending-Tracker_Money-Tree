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

def select_by_group_merchant(values):
    merchants = []
    sql = '''Select id, amount
            from merchants
            full outer join
            (SELECT t.merchant_id as merchant_id, sum(t.amount) as amount 
            FROM transactions as t
            right JOIN merchants as m
            ON t.merchant_id = m.id
            WHERE EXTRACT(MONTH FROM transaction_date) = %s
            AND EXTRACT(YEAR FROM transaction_date) = %s
            group by m.name, t.merchant_id)
            as totals
            on merchants.id = totals.merchant_id
            order by activated desc, (amount is null), name
            '''
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
        merchant = merchant_repository.select(row['id'])
        amount = (row['amount'])
        merchants.append([merchant,amount])
    return merchants, total

def select_by_group_category(values):
    categories = []
    sql = '''Select id, amount
            from categories
            full outer join
            (SELECT t.category_id as category_id, sum(t.amount) as amount 
            FROM transactions as t
            right JOIN categories as c
            ON t.category_id = c.id
            WHERE EXTRACT(MONTH FROM transaction_date) = %s
            AND EXTRACT(YEAR FROM transaction_date) = %s
            group by c.name, t.category_id)
            as totals
            on categories.id = totals.category_id
            order by activated desc, (amount is null), name
            '''
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
        category = category_repository.select(row['id'])
        amount = (row['amount'])
        categories.append([category,amount])
    return categories, total


def select_all_merchant(merchant,sort):
    
    transactions = []
    values = [merchant.id]
 
    if sort == 'transaction_date':
        sql = "SELECT * FROM transactions where merchant_id = %s order by transaction_date desc"
            
    elif sort == 'merchant_id':
        sql = "SELECT * FROM transactions where merchant_id = %s order by transaction_date desc"

    elif sort == 'category_id':
        sql = '''SELECT * FROM transactions as t
                JOIN categories as c
                ON t.category_id = c.id
                where merchant_id = %s order by c.name'''
    else: 
        sort == 'amount'
        sql = "SELECT * FROM transactions where merchant_id = %s order by amount desc"

    results = run_sql(sql, values)
    
    
    sql_total = '''SELECT sum(amount)
                FROM transactions
                where merchant_id = %s'''
    
    total = run_sql(sql_total, values)[0]

    for row in results:
        category = category_repository.select(row['category_id'])
        transaction = Transaction(row['transaction_date'], merchant, row['amount'],category, id)
        transactions.append(transaction)
    return transactions,total


def select_all_category(category,sort):
    
    transactions = []
    values = [category.id]
 
    if sort == 'transaction_date':
        sql = "SELECT * FROM transactions where category_id = %s order by transaction_date desc"
            
    elif sort == 'merchant_id':
        sql = '''SELECT * FROM transactions as t
                JOIN merchants as m
                ON t.category_id = m.id
                where category_id = %s order by m.name'''


    elif sort == 'category_id':
        sql = "SELECT * FROM transactions where category_id = %s order by transaction_date desc"
    
    else: 
        sort == 'amount'
        sql = "SELECT * FROM transactions where category_id = %s order by amount desc"

    results = run_sql(sql, values)
    
    
    sql_total = '''SELECT sum(amount)
                FROM transactions
                where category_id = %s'''
    
    total = run_sql(sql_total, values)[0]

    for row in results:
        merchant = merchant_repository.select(row['merchant_id'])
        transaction = Transaction(row['transaction_date'], merchant, row['amount'],category, id)
        transactions.append(transaction)
    return transactions,total
    
    
    






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
    