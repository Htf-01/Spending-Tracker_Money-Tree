from flask import Flask, render_template, session

from models.budget import Budget

# Import Controllers
from controllers.transaction_controller import transaction_blueprint
from controllers.merchant_controller import merchant_blueprint
from controllers.category_controller import category_blueprint
from controllers.budget_controller import budget_blueprint


app = Flask(__name__)

app.secret_key = 'BAD_SECRET_KEY0'

# Import Blueprints
app.register_blueprint(transaction_blueprint)
app.register_blueprint(merchant_blueprint)
app.register_blueprint(category_blueprint)
app.register_blueprint(budget_blueprint)

@app.route('/')
def home():

    session['date'] = {'month':(Budget.today().month), 'year':(Budget.today().year)}
    session['current'] = {'month':(Budget.today().month), 'year':(Budget.today().year)}
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)