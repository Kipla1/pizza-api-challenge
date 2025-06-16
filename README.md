# Pizza Restaurant API

A Flask-based REST API for managing pizza restaurants and their menus.

## Description

This API allows you to manage restaurants, pizzas, and their relationships. You can:
- View all restaurants
- View restaurant details with their pizzas
- Delete restaurants
- View all pizzas
- Create restaurant-pizza relationships


## Setup Instructions

1. **Install dependencies:**
    ```sh
    pipenv install
    ```

2. **Activate the virtual environment:**
    ```sh
    pipenv shell
    ```

3. **Run database migrations:**
    ```sh
    flask db upgrade
    ```

4. **Seed the database:**
    ```sh
    python server/seed.py
    ```

5. **Start the development server:**
    ```sh
    python server/app.py
    ```

## API Endpoints

### Restaurants

- `GET /restaurants`  
  List all restaurants.

- `GET /restaurants/<id>`  
  Get a restaurant and its pizzas.

- `DELETE /restaurants/<id>`  
  Delete a restaurant and its menu items.

### Pizzas

- `GET /pizzas`  
  List all pizzas.

### Restaurant Pizzas

- `POST /restaurant_pizzas`  
  Add a pizza to a restaurant's menu.  
  **Body:**  
  ```json
  {
    "price": 10,
    "pizza_id": 1,
    "restaurant_id": 2
  }
  ```

## Tecnologies
* Python 3.8
* Flask
* Flask-SQLAlchemy
* Flask-Migrate  