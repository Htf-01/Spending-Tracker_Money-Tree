from hashlib import new
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
    merchants = merchant_repository.select_all()
    categories = category_repository.select_all()
    return render_template("transactions/index.html", all_transactions = transactions, all_merchants = merchants, all_categories = categories)

# New   - Not currently using. New Task is on the main page (it's the primary function')
# @transaction_blueprint.route("/transactions/new", methods = ['GET'])
# def new_transaction():
#     merchants = merchant_repository.select_all()
#     categories = category_repository.select_all()
#     transactions = transaction_repository.select_all()
#     return render_template("transactions/new.html", all_transactions = transactions, all_merchants = merchants, all_categories = categories)

# Create

# POST '/tasks'
@transaction_blueprint.route("/transactions", methods = ['POST'])
def create_transaction():
    date = request.form['date']
    
    merchant = merchant_repository.select_by_name(request.form['merchant'])
    category = category_repository.select_by_name(request.form['category'])
    
    # breakpoint()
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
# Update
# Delete