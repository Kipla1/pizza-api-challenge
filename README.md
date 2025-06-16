# Pizza Restaurant API

A Flask-based REST API for managing pizza restaurants and their menus. This API allows you to manage restaurants, pizzas, and their relationships through a many-to-many association.

## Features

- View all restaurants
- View restaurant details with their pizzas
- Delete restaurants (with cascade delete of menu items)
- View all available pizzas
- Create restaurant-pizza relationships with pricing

## Prerequisites

- Python 3.8
- pipenv
- SQLAlchemy
- Flask

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Kipla1/pizza-api-challenge
cd pizza-api-challenge
```

### 2. Install Dependencies with Pipenv
```bash
# Install pipenv if you haven't already
pip install pipenv

# Install project dependencies
pipenv install
```

### 3. Activate Virtual Environment
```bash
pipenv shell
```

### 4. Database Setup & Migration
```bash
# Create initial migration (if migrations folder doesn't exist)
flask db init

# Create migration files
flask db migrate -m "Initial migration"

# Apply migrations to create tables
flask db upgrade
```

### 5. Seed the Database
```bash
# Run the seed script to populate with sample data
python server/seed.py
```

### 6. Start the Development Server
```bash
# Run the Flask application
python server/app.py
```

The API will be available at `http://localhost:5000`


## API Routes Summary

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/restaurants` | Get all restaurants | No |
| GET | `/restaurants/<id>` | Get restaurant by ID with pizzas | No |
| DELETE | `/restaurants/<id>` | Delete restaurant | No |
| GET | `/pizzas` | Get all pizzas | No |
| POST | `/restaurant_pizzas` | Add pizza to restaurant menu | No |

## API Documentation

### Restaurants

#### GET /restaurants
Get all restaurants

**Request:**
```http
GET /restaurants HTTP/1.1
Host: localhost:5000
Content-Type: application/json
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "Dominion Pizza",
    "address": "Good Italian, Ngong Road, 5th Avenue"
  },
  {
    "id": 2,
    "name": "Pizza Hut",
    "address": "Westgate Mall, Mwanzi Road, Nrb 100"
  },
  {
    "id": 3,
    "name": "Kiki's Pizza",
    "address": "Forest Road, Nairobi"
  }
]
```

#### GET /restaurants/<id>
Get a specific restaurant with its pizzas

**Request:**
```http
GET /restaurants/1 HTTP/1.1
Host: localhost:5000
Content-Type: application/json
```

**Response (Success):**
```json
{
  "id": 1,
  "name": "Dominion Pizza",
  "address": "Good Italian, Ngong Road, 5th Avenue",
  "restaurant_pizzas": [
    {
      "id": 1,
      "price": 10,
      "pizza": {
        "id": 1,
        "name": "Cheese",
        "ingredients": "Dough, Tomato Sauce, Cheese"
      }
    },
    {
      "id": 2,
      "price": 15,
      "pizza": {
        "id": 2,
        "name": "Pepperoni",
        "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
      }
    }
  ]
}
```

**Response (Not Found):**
```json
{
  "error": "Restaurant not found"
}
```

#### DELETE /restaurants/<id>
Delete a restaurant and its menu items

**Request:**
```http
DELETE /restaurants/1 HTTP/1.1
Host: localhost:5000
```

**Response (Success):**
```http
HTTP/1.1 204 No Content
```

**Response (Not Found):**
```json
{
  "error": "Restaurant not found"
}
```

### Pizzas

#### GET /pizzas
Get all available pizzas

**Request:**
```http
GET /pizzas HTTP/1.1
Host: localhost:5000
Content-Type: application/json
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  },
  {
    "id": 3,
    "name": "California",
    "ingredients": "Dough, Sauce, Ricotta, Red peppers, Mustard"
  }
]
```

### Restaurant Pizzas

#### POST /restaurant_pizzas
Add a pizza to a restaurant's menu with pricing

**Request:**
```http
POST /restaurant_pizzas HTTP/1.1
Host: localhost:5000
Content-Type: application/json

{
  "price": 12,
  "pizza_id": 1,
  "restaurant_id": 2
}
```

**Response (Success):**
```json
{
  "id": 7,
  "price": 12,
  "pizza_id": 1,
  "restaurant_id": 2,
  "pizza": {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  "restaurant": {
    "id": 2,
    "name": "Pizza Hut",
    "address": "Westgate Mall, Mwanzi Road, Nrb 100"
  }
}
```

**Response (Validation Error):**
```json
{
  "errors": ["Price must be between 1 and 30"]
}
```

**Response (Missing Fields):**
```json
{
  "error": ["Missing required fields: price, pizza_id, restaurant_id"]
}
```

**Response (Not Found):**
```json
{
  "error": ["Restaurant not found"]
}
```
or
```json
{
  "error": ["Pizza not found"]
}
```

## Validation Rules

### RestaurantPizza Validation
- **price**: Required, must be an integer between 1 and 30 (inclusive)
- **pizza_id**: Required, must be a valid Pizza ID
- **restaurant_id**: Required, must be a valid Restaurant ID

### Restaurant Validation
- **name**: Required, maximum 100 characters
- **address**: Required, maximum 200 characters

### Pizza Validation
- **name**: Required, maximum 100 characters
- **ingredients**: Required, maximum 1000 characters

## Error Responses

### Common HTTP Status Codes
- `200` - Success
- `201` - Created
- `204` - No Content (for successful DELETE)
- `400` - Bad Request (validation errors)
- `404` - Not Found

### Error Response Format
```json
{
  "error": "Error message"
}
```

or for validation errors:
```json
{
  "errors": ["Error message 1", "Error message 2"]
}
```

## Postman Usage Instructions

### 1. Set Up Environment
Create a new environment in Postman with:
- `base_url`: `http://localhost:5000`

### 2. Import Collection
Create a new collection and add the following requests:

#### Get All Restaurants
```
GET {{base_url}}/restaurants
```

#### Get Restaurant by ID
```
GET {{base_url}}/restaurants/1
```

#### Delete Restaurant
```
DELETE {{base_url}}/restaurants/1
```

#### Get All Pizzas
```
GET {{base_url}}/pizzas
```

#### Create Restaurant Pizza
```
POST {{base_url}}/restaurant_pizzas
Content-Type: application/json

{
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 2
}
```

### 3. Test Scenarios

#### Valid Restaurant Pizza Creation
```json
{
  "price": 12,
  "pizza_id": 1,
  "restaurant_id": 1
}
```

#### Invalid Price (should return error)
```json
{
  "price": 35,
  "pizza_id": 1,
  "restaurant_id": 1
}
```

#### Missing Fields (should return error)
```json
{
  "price": 12
}
```

## Database Migration & Seeding

### Creating New Migrations
```bash
# After making model changes
flask db migrate -m "Description of changes"

# Apply the migration
flask db upgrade
```

### Rolling Back Migrations
```bash
# Rollback to previous migration
flask db downgrade
```

### Re-seeding the Database
```bash
# Clear and re-populate with sample data
python server/seed.py
```

### Sample Data Included
After seeding, the database will contain:
- 3 restaurants (Dominion Pizza, Pizza Hut, Kiki's Pizza)
- 3 pizzas (Cheese, Pepperoni, California)
- 6 restaurant-pizza relationships with various prices

## Technologies Used

- **Python 3.8+**
- **Flask** - Web framework
- **Flask-SQLAlchemy** - ORM for database operations
- **Flask-Migrate** - Database migration management
- **SQLite** - Database (default)

## Project Structure

```
pizza-restaurant-api/
├── server/
│   ├── controllers/
│   │   ├── pizza_controller.py
│   │   ├── restaurant_controller.py
│   │   └── restaurant_pizza_controller.py
│   ├── models/
│   │   ├── pizza.py
│   │   ├── restaurant.py
│   │   └── restaurant_pizza.py
│   ├── app.py
│   ├── config.py
│   └── seed.py
├── migrations/
├── pizza_restaurant.db
├── Pipfile
├── Pipfile.lock
└── README.md
```

## Development Notes

### Known Issues
1. There's a typo in `restaurant_pizza_controller.py` - `method=['POST']` should be `methods=['POST']`
2. Some model relationships need to be fixed (typos in foreign key names)
3. Missing return statements in some error cases

### Future Enhancements
- Add authentication and authorization
- Implement pagination for large datasets
- Add search and filtering capabilities
- Include comprehensive error logging
- Add API rate limiting
- Implement caching for better performance

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License.