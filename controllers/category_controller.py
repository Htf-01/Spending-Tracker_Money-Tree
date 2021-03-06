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
    if category_total == [None]:
        category_total = ['000'] 
    


    return render_template("categories/index.html",
                           groups = category_groups,
                           date = date,
                           total = category_total,
                           title = 'Categories')

# New

# Create    
@category_blueprint.route("/categories", methods = ['POST'])
def create_category():

    category = category_repository.select_by_name(request.form['name'])

    if category == False:
        category_repository.save(Category(request.form['name']))
    
    return redirect('/categories')

# Show

@category_blueprint.route("/categories/<id>", methods = ['GET'])
def show_category(id):

    category = category_repository.select(id)
    
    title = category.name
    
    sort = Transaction.session_return_sort(session)
    transactions = transaction_repository.select_all_category(category,sort)[0]
    total = transaction_repository.select_all_category(category,sort)[1]
    if total == [None]:
        total = ['000']  
    

    
    return render_template("categories/show.html",
                           category = category,
                           transactions = transactions,
                           total = total,
                           title =  title)







# Edit
# Update
@category_blueprint.route("/categories/<id>", methods = ['POST'])
def update_category(id):
    
    if request.form['action'] == 'action':
        category = category_repository.select(id)
        category_repository.update_activated(category)

    return redirect('/categories')

# Delete

# Session Sort

@category_blueprint.route("/categories/<id>/sort", methods = ['POST'])
def sort_transactions_categories(id):
    
    # Which button was pressed
    sort = request.form['button']
    Transaction.session_edit_sort(session,sort)
    
    return redirect(f'/categories/{id}')




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





