from server.app import db
from sqlalchemy.orm import validates

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    
    # Foreign Keys
    restaurants_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizzas_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
    
    # Relationship
    pizza = db.relationship('Pizza', backref='restaurant_pizzas')
    
    # VAlidation
    @validates
    def validate_price(self, key, price):
        if price < 1 or price > 30:
            raise ValueError("Price must be between 1 and 30")
        return price