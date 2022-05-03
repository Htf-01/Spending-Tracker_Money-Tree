from flask import Flask, render_template, session




# Import Controllers
from controllers.transaction_controller import transaction_blueprint
from controllers.merchant_controller import merchant_blueprint
from controllers.category_controller import category_blueprint
from models.transaction import Transaction



app = Flask(__name__)

app.secret_key = 'BAD_SECRET_KEY'

# Upload folder
UPLOAD_FOLDER = 'static/files'
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

# Import Blueprints
app.register_blueprint(transaction_blueprint)
app.register_blueprint(merchant_blueprint)
app.register_blueprint(category_blueprint)


@app.route('/')
def home():

    session['date'] = {'month':(Transaction.session_today().month), 'year':(Transaction.session_today().year)}
    session['current'] = {'month':(Transaction.session_today().month), 'year':(Transaction.session_today().year)}
    session['sort']={'sort':'transaction_date'}
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)