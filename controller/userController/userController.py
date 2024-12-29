from flask import Blueprint

# Create a Blueprint instance
user_controller = Blueprint('user_controller', __name__)

from models.usermodel.usermodel import user_model 

obj = user_model() 

@user_controller.route('/users')
def user_homepage():
    return obj.user_signup(); 
