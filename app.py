from flask import Flask #Importing the Flask class from the flask module

app = Flask(__name__) #Creating an instance of the Flask class, which will be our WSGI application. The __name__ variable is passed to the Flask constructor to determine the root path of the application. This is necessary for finding resources and templates.

@app.route('/') #The @app.route('/') decorator is used to bind a function to a specific URL. In this case, it binds the home() function to the root URL ('/'). When a user accesses the root URL of the application, the home() function will be executed.

def home(): #function creation to return a string when the root URL is accessed
    return "DevOps CI/CD Pipeline Running successfully" 

if __name__ == "__main__": #main block to run the application. This ensures that the Flask application will only run if this script is executed directly, and not when it is imported as a module in another script.
    app.run(host="0.0.0.0", port=5000)