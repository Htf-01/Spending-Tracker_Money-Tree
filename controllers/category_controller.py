from flask import Flask, Blueprint, render_template, redirect, request

from repositories import category_repository

from models.category import Category


category_blueprint = Blueprint("categories", __name__)

# Index
@category_blueprint.route("/categories")
def categories():

    categories = category_repository.select_all()

    return render_template("categories/index.html", all_categories = categories)

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





