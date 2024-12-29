from flask import Blueprint 

product_controller = Blueprint('product_controller', __name__) 

@product_controller.route('/products') 

def all_products(): 
    return 'This is the add products homepage'