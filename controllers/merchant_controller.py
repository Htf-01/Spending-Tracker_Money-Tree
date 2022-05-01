from flask import Flask, Blueprint, render_template, redirect, request

from repositories import merchant_repository

from models.merchant import Merchant


merchant_blueprint = Blueprint("merchants", __name__)

# Index
@merchant_blueprint.route("/merchants")
def merchants():

    merchants = merchant_repository.select_all()

    return render_template("merchants/index.html", all_merchants = merchants)

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





