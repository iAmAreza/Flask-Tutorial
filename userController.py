from flask import Blueprint

# Create a Blueprint instance
user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/users')
def user_homepage():
    return 'This is the user homepage'
