# Import  the Framework
from flask import Flask
from flask_restful import Api

from .connection import get_connection
from .user_controller import User
from .user_controller import Users

# Create the instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)

api.add_resource(Users, '/users')
api.add_resource(User, '/users/<string:id>')
