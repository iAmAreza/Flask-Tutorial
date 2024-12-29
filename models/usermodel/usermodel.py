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
      self.con.autocommit = True ## very very crucial line as it is responsible for the auto commit of the database. without this line, the database will not be updated.
    except:
      print('Database connection error')
    

  def user_signup(self): 
    self.cursor.execute('SELECT * FROM users') 
    result = self.cursor.fetchall() 
    result = json.dumps(result)  
    return result   
  

  def adduser(self, data):
    print(data)
    # Corrected SQL query and parameter passing
    query = '''
        INSERT INTO users (name, email, phone, password, role) 
        VALUES (%s, %s, %s, %s, %s)
    '''
    # Explicitly converting data['name'] to string
    self.cursor.execute(query, (
        str(data['name']),       # Convert to string
        data['email'], 
        data['phone'], 
        data['password'], 
        data['role']
    ))
    return "User added successfully, hurrah!!"
  
  def updateuser(self, data):
    print(data); 
    query = '''
        UPDATE users
        SET name = %s, email = %s, phone = %s, password = %s, role = %s
        WHERE id = %s
    '''
    self.cursor.execute(query, (
        str(data['name']),       # Convert name to string (if necessary)
        str(data['email']),      # Convert email to string (if necessary)
        str(data['phone']),      # Convert phone to string (if necessary)
        str(data['password']),   # Convert password to string (if necessary)
        str(data['role']),       # Convert role to string (if necessary)
        data['id']          # user_id as an integer (matching the 'id' column in users table)
    ))
    return "User updated successfully!"
  

  def deleteuser(self, id):
    print(id)
    query = '''
        DELETE FROM users
        WHERE id = %s
    '''
    self.cursor.execute(query, (id,))
    return "User deleted successfully!"

