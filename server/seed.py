from server.app import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

def seed_data():
    with app.app_context():
        # Clear existing data
        print("Clearing existing data...")
        RestaurantPizza.query.delete()
        Restaurant.query.delete()
        Pizza.query.delete()
        
        # Create restaurants
        print("Creating restaurants...")
        restaurants = [
            Restaurant(name="Dominion Pizza", address="Good Italian, Ngong Road, 5th Avenue"),
            Restaurant(name="Pizza Hut", address="Westgate Mall, Mwanzi Road, Nrb 100"),
            Restaurant(name="Kiki's Pizza", address="Forest Road, Nairobi")
        ]
        
        for restaurant in restaurants:
            db.session.add(restaurant)
        
        # Create pizzas
        print("Creating pizzas...")
        pizzas = [
            Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese"),
            Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni"),
            Pizza(name="California", ingredients="Dough, Sauce, Ricotta, Red peppers, Mustard")
        ]
        
        for pizza in pizzas:
            db.session.add(pizza)
        
        # Commit to get IDs
        db.session.commit()
        
        # Create restaurant-pizza relationships
        print("Creating restaurant-pizza relationships...")
        restaurant_pizzas = [
            RestaurantPizza(price=10, restaurant_id=1, pizza_id=1),
            RestaurantPizza(price=15, restaurant_id=1, pizza_id=2),
            RestaurantPizza(price=12, restaurant_id=2, pizza_id=1),
            RestaurantPizza(price=18, restaurant_id=2, pizza_id=3),
            RestaurantPizza(price=8, restaurant_id=3, pizza_id=1),
            RestaurantPizza(price=20, restaurant_id=3, pizza_id=3)
        ]
        
        for rp in restaurant_pizzas:
            db.session.add(rp)
        
        db.session.commit()
        print("Seed data created successfully!")

if __name__ == '__main__':
    seed_data()