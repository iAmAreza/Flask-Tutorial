from flask import Flask;

app = Flask(__name__); 

@app.route('/') 
def welcome():
    return 'Welcome to the Flask World!';  

@app.route('/home') 

def home():
    return 'This is the home page'; 

if __name__ == '__main__': 
    app.run(debug=True); 