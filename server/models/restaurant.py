from app import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    
    # def __init__(self, name, address):
        # self.name = name
        # self.address = address
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    
    # Relationship with cascade delete
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant', cascade='all, delete-orphan')