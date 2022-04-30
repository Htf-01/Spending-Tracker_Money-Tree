from flask import Flask, Blueprint, render_template, redirect, request
from repositories import transaction_repository
from repositories import merchant_repository
from repositories import category_repository

from models.transaction import Transaction
from models.merchant import Merchant
from models.category import Category

transaction_blueprint = Blueprint("transactions", __name__)

# Index

@transaction_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    # merchants = merchant_repository.select_all()
    # categories = category_repository.select_all()
    # breakpoint()
    return render_template("transactions/index.html", all_transactions = transactions)#, all_merchants = merchants, all_categories = categories)


@transaction_blueprint.route("/transactions/new", methods = ['GET'])
def new_transaction():
    merchants = merchant_repository.select_all()
    categories = category_repository.select_all()
    transactions = transaction_repository.select_all()
    return render_template("transactions/new.html", all_transactions = transactions, all_merchants = merchants, all_categories = categories)

# Create

# POST '/tasks'
@transaction_blueprint.route("/transactions/new", methods = ['POST'])
def create_transaction():
    date = request.form['date']
    
    merchant = merchant_repository.select_by_name(request.form['merchant'])
    category = category_repository.select_by_name(request.form['category'])
    
    if merchant == False:
        merchant = merchant_repository.select(merchant_repository.save(Merchant(request.form['merchant'])))
    
    if category == False:
        category = category_repository.select(category_repository.save(Category(request.form['category'])))
        
    amount = (request.form['amount_pound']) + (request.form['amount_pence'])
    
    transaction = Transaction(date, merchant,amount,category)

    transaction_repository.save(transaction)
    return redirect('/transactions')

# Show

# Edit
@transaction_blueprint.route("/transactions/<id>/edit", methods = ['GET'])
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    merchants = merchant_repository.select_all()
    categories = category_repository.select_all()
    transactions = transaction_repository.select_all()
    return render_template('transactions/edit.html', transaction = transaction, all_transactions = transactions, all_merchants = merchants, all_categories = categories)

# Update
@transaction_blueprint.route("/transactions/<id>", methods = ['POST'])
def update_transactions(id):
    date = request.form['date']
    
    merchant = merchant_repository.select_by_name(request.form['merchant'])
    category = category_repository.select_by_name(request.form['category'])
    
    if merchant == False:
        merchant = merchant_repository.select(merchant_repository.save(Merchant(request.form['merchant'])))
    
    if category == False:
        category = category_repository.select(category_repository.save(Category(request.form['category'])))
        
        
        
    budget_id = transaction_repository.select_budget((Transaction.string_to_date(date)))
    amount = (request.form['amount_pound']) + (request.form['amount_pence'])
    
    transaction = Transaction(date, merchant,amount,category, budget_id, id)

    transaction_repository.update(transaction)
    return redirect('/transactions')



# Delete
@transaction_blueprint.route("/transactions/<id>/delete", methods = ['GET'])
def delete_confrim(id):
    transaction = transaction_repository.select(id)
    merchants = merchant_repository.select_all()
    categories = category_repository.select_all()
    transactions = transaction_repository.select_all()
    return render_template('transactions/delete.html', transaction = transaction, all_transactions = transactions, all_merchants = merchants, all_categories = categories)

@transaction_blueprint.route("/transactions/<id>/delete", methods = ['POST'])
def delete_transaction(id):

    transaction_repository.delete(id)
    return redirect('/transactions')


##################################################

@transaction_blueprint.route("/transactions/sort", methods = ['POST'])
def sort_transactions():
    
    # Which button was pressed
    Transaction.sort = request.form['button']
    return redirect('/transactions')
