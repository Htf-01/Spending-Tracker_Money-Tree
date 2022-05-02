from flask import Flask, Blueprint, render_template, redirect, request, session

from repositories import budget_repository


from models.budget import Budget
from models.transaction import Transaction


budget_blueprint = Blueprint("budget", __name__)


@budget_blueprint.route("/budget")
def budget():
    
    budget = budget_repository.get_current_budget()

    return redirect (f'/budget/{budget}')

@budget_blueprint.route("/budget/<id>", methods = ['GET'])
def show_budget(id):
    # breakpoint()
    
    Budget.set_current_budget(id)
    
    today = budget_repository.select_budget(Budget.today())
  
    display_date = f'{Transaction.number_to_month(session["date"]["month"])} {session["date"]["year"]}'
        
    
    date = budget_repository.select_date(id)
    date_display =Budget.date_format_display(date)
    date_picker =Budget.date_format_picker(date)
    
    budget = budget_repository.get_current_budget()

    breakpoint()
    
    return render_template("budget/current.html", today = today, budget = budget, date_display = date_display, date_picker = date_picker)

@budget_blueprint.route("/budget/<id>/redirect", methods = ['POST'])
def redirect_budget(id):

    date = Budget.convert_date(request.form['date'])
    budget = budget_repository.select_budget(date)


    return redirect (f'/budget/{budget}')