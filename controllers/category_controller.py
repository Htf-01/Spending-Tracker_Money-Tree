from flask import Flask, Blueprint, render_template, redirect, request, session

from repositories import category_repository
from repositories import transaction_repository

from models.category import Category
from models.transaction import Transaction


category_blueprint = Blueprint("categories", __name__)

# Index
@category_blueprint.route("/categories")
def categories():

    date = Transaction.session_date_display(session)
    date_values = Transaction.session_sql_format(session)
    
    category_groups = transaction_repository.select_by_group_category(date_values)[0]
    category_total = transaction_repository.select_by_group_category(date_values)[1]

    return render_template("categories/index.html", groups = category_groups, date = date, total = category_total)

# New

# Create    
@category_blueprint.route("/categories", methods = ['POST'])
def create_category():

    category = category_repository.select_by_name(request.form['name'])

    if category == False:
        category_repository.save(Category(request.form['name']))
    
    return redirect('/categories')

# Show
# Edit
# Update
@category_blueprint.route("/categories/<id>", methods = ['POST'])
def update_category(id):
    
    if request.form['action'] == 'action':
        category = category_repository.select(id)
        category_repository.update_activated(category)

    return redirect('/categories')

# Delete


#  SESSION HANDLING - Month View

@category_blueprint.route("/categories/nextmonth")
def categories_next_month():
    
    Transaction.session_increment(session)
    
    return redirect('/categories')

@category_blueprint.route("/categories/previousmonth")
def categories_previous_month():
    
    Transaction.session_decrement(session)
    
    return redirect('/categories')

@category_blueprint.route("/categories/currentmonth")
def categories_current_month():
    
    Transaction.session_current(session)
    
    return redirect('/categories')

@category_blueprint.route("/categories/month", methods = ['POST'])
def categories_select_month():
    
    date_string = request.form['date']
    
    Transaction.session_select(session,date_string)
    
    return redirect('/categories')





