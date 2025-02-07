from models import Product
from app import app, db

with app.app_context():
    db.drop_all()
    db.create_all()
    Product1 = Product(name="Механічна клавіатура", price=3000.0)
    Product2 = Product(name="Мембранна клавіатура", price=1500.0)
    Product3 = Product(name="Оптично-механічна клавіатура",  price=5000.0)
    db.session.add_all([Product1, Product2, Product3])
    db.session.commit()