from flask import Blueprint
from flask import request
# Create a Blueprint instance
user_controller = Blueprint('user_controller', __name__)

from models.usermodel.usermodel import user_model 

obj = user_model() 

# this is for get all user 
@user_controller.route('/users')
def user_homepage():
    return obj.user_signup(); 

#creating user 
@user_controller.route('/users/adduser',methods=['POST']) 

def adduser(): 
    newdata = request.form    
    return obj.adduser(newdata);   

#updating user 

@user_controller.route('/users/updateuser',methods=['PUT']) 

def updateuser():
    newdata = request.form  
    
    return obj.updateuser(newdata); 
 
#deleting user 

@user_controller.route('/users/deleteuser/<id>',methods=['DELETE']) 

def deleteuser(id):

    return obj.deleteuser(id);