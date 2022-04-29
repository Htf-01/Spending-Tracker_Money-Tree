from flask import Flask, render_template

# Import Controllers
from controllers.transaction_controller import transaction_blueprint


app = Flask(__name__)

# Import Blueprints
app.register_blueprint(transaction_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)