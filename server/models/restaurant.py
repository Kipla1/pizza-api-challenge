from server.app import db

class Restaurant:
    __tablename__ = 'restaurants'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    
    # Relationship with cascade delete
    restaurant_pizzas = db.relationship('ResaurantPizza', backref='restaurant', cascade='all, delete-orphan')