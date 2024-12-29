import mysql.connector 
import json
class user_model():

  def __init__(self):
    try:
      self.con = mysql.connector.connect(host='localhost',
                                  database='user_db',user='root', 
                                  password='root')
      print('Database connection established') 
      self.cursor = self.con.cursor(dictionary=True) 
    except:
      print('Database connection error')
    

  def user_signup(self): 
    self.cursor.execute('SELECT * FROM users') 
    result = self.cursor.fetchall() 
    result = json.dumps(result)  
    return result  