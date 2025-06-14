from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from models import db
from config import Config

# Create Flask App Instance
app = Flask(__name__)

# Load configuration
app.config.from_object(Config)

# Initialize db
db = SQLAlchemy(app)

# Initialize migrations
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True, port=5555)