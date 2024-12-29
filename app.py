from flask import Flask
from controller.userController.userController import user_controller  # Import the Blueprint
from controller.productController.productController import product_controller  # Import the Blueprint 
app = Flask(__name__)

# Register the Blueprint

app.register_blueprint(user_controller)
app.register_blueprint(product_controller)

@app.route('/')
def welcome():
    return 'Welcome to the Flask World!'

@app.route('/home')
def home():
    return 'This is the home page'

if __name__ == '__main__':
    app.run(debug=True)
