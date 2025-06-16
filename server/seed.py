from app import app, db
from models.pizza import Pizza
from models.restaurant import Restaurant
from models.restaurant_pizza import RestaurantPizza

def seed_data():
    with app.app_context():
        # Clear existing data
        RestaurantPizza.query.delete()
        Restaurant.query.delete()
        Pizza.query.delete()

        # Seed Pizzas
        pizza1 = Pizza(name="Mara", ingredients="Tomato, Mozzarella, Basil")
        pizza2 = Pizza(name="Pepperoni", ingredients="Pepperoni, Tomato, Mozzarella")
        db.session.add_all([pizza1, pizza2])
        db.session.commit()

        # Seed Restaurants
        restaurant1 = Restaurant(name="Pizza Place", address="123 Main St")
        restaurant2 = Restaurant(name="Pizza Palace", address="456 Elm St")
        db.session.add_all([restaurant1, restaurant2])
        db.session.commit()

        # Seed RestaurantPizzas
        restaurant_pizza1 = RestaurantPizza(price=10, pizza_id=pizza1.id, restaurant_id=restaurant1.id)
        restaurant_pizza2 = RestaurantPizza(price=12, pizza_id=pizza2.id, restaurant_id=restaurant2.id)
        db.session.add_all([restaurant_pizza1, restaurant_pizza2])
        db.session.commit()

        print("Data seeded successfully!")

if __name__ == "__main__":
    seed_data()