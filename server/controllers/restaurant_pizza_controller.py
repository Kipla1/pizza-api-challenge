from flask import Blueprint, request, jsonify
from server.app import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data or 'price' not in data or 'pizza_id' not in data or 'restaurant_id' not in data:
            return jsonify({'error': ['Missing required fiels: price, pizza_id, restaurant_id']})
        
        # Check if restaurant and pizza exist
        restaurant = Restaurant.query.get(data['restaurant_id'])
        pizza = Pizza.query.get(data['pizza_id'])
        
        if not restaurant:
            return jsonify({'error': 'Restaurant not found'}), 404
            
        if not pizza:
            return jsonify({'error': 'Pizza not found'}), 404
            
        # Create new RestaurantPizza(Validation happens automatically)
        restaurant_pizza = RestaurantPizza(
            price = data['price'],
            pizza_id = data['pizza_id'],
            restaurant_id = data['restaurant_id']
        )        
        db.session.add(restaurant_pizza)
        db.session.commit()
        
        # return response with full details
        return jsonify({
             'id': restaurant_pizza.id,
            'price': restaurant_pizza.price,
            'pizza_id': restaurant_pizza.pizza_id,
            'restaurant_id': restaurant_pizza.restaurant_id,
            'pizza': {
                'id': pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients
            },
            'restaurant': {
                'id': restaurant.id,
                'name': restaurant.name,
                'address': restaurant.address
            }
        }), 201
        
    except ValueError as e:
        return jsonify({'errors': [str(e)]}), 400
    except Exception as e:
        return jsonify({'errors': 'An error occured while creating restaurant pizza'}), 400