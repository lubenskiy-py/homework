from flask import Flask, render_template
from models import db, Product



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)


@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)


@app.route('/buy-item', methods=['POST'])
def buy_item():
    return render_template('payment.html')


@app.route('/submit_payment', methods=['POST'])
def submit_payment():
    return "Дякуємо за покупку"




if __name__ == '__main__':
    app.run(debug=True)
