
from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/')
def homePage():
    url_for('/register')
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def loginPage():
    # Handle user login
    # Validate user credentials and generate a session token
    pass


@app.route('/login', methods=['POST'])
def loginPage():
    # Handle user login
    # Validate user credentials and generate a session token
    pass


@app.route('/lobby', methods=['GET'])
def lobby():
    # Display the main lobby page where users can create or enter chat rooms
    pass

@app.route('/chat/<room>', methods=['GET'])
def chat_room(room):
    # Display the specified chat room with all messages sent
    pass



# Main function to run the application
if __name__ == '__main__':
   app.run(host="0.0.0.0")

