from flask import Flask, Blueprint, render_template, redirect, request, session

from repositories import merchant_repository
from repositories import transaction_repository

from models.merchant import Merchant
from models.transaction import Transaction


merchant_blueprint = Blueprint("merchants", __name__)

# Index
@merchant_blueprint.route("/merchants")
def merchants():


    date = Transaction.session_date_display(session)
    date_values = Transaction.session_sql_format(session)
    
    merchant_groups = transaction_repository.select_by_group_merchant(date_values)[0]
    merchant_total = transaction_repository.select_by_group_merchant(date_values)[1]

 
    
    return render_template("merchants/index.html",  groups = merchant_groups, date = date, total = merchant_total)

# New

# Create
@merchant_blueprint.route("/merchants", methods = ['POST'])
def create_merchant():

    merchant = merchant_repository.select_by_name(request.form['name'])

    if merchant == False:
        merchant_repository.save(Merchant(request.form['name']))
    
    return redirect('/merchants')

# Show






# Edit
# Update
@merchant_blueprint.route("/merchants/<id>", methods = ['POST'])
def update_merchant(id):
    
    if request.form['action'] == 'action':
        merchant = merchant_repository.select(id)
        merchant_repository.update_activated(merchant)

    return redirect('/merchants')

# Delete


# Session Handling

@merchant_blueprint.route("/merchants/nextmonth")
def merchants_next_month():
    
    Transaction.session_increment(session)
    
    return redirect('/merchants')

@merchant_blueprint.route("/merchants/previousmonth")
def merchants_previous_month():
    
    Transaction.session_decrement(session)
    
    return redirect('/merchants')

@merchant_blueprint.route("/merchants/currentmonth")
def merchants_current_month():
    
    Transaction.session_current(session)
    
    return redirect('/merchants')

@merchant_blueprint.route("/merchants/month", methods = ['POST'])
def merchants_select_month():
    
    date_string = request.form['date']
    
    Transaction.session_select(session,date_string)
    
    return redirect('/merchants')





