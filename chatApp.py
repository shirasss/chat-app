
from flask import Flask, render_template,session,request
from tkinter import messagebox
app = Flask(__name__)
 
@app.route('/')
def homePage():
    return render_template('register.html')
if __name__ == '__main__':
   app.run(host="0.0.0.0")






@app.route('/login', methods=['POST'])
def loginPage():
    # Handle user login
    # Validate user credentials and generate a session token
    pass

@app.route('/logout', methods=['POST'])
def logOut():
    session.pop('username', 'password')
    messagebox.showinfo('Logout successfull') #alert
    return Flask.redirect(url_for('login'))


@app.route('/lobby', methods=['GET'])
def lobby():
    # Display the main lobby page where users can create or enter chat rooms
    #for room in 

    
    pass

@app.route('/chat/<room>', methods=['GET'])
def chat_room(room):
    # Display the specified chat room with all messages sent
    pass



# Main function to run the application
if __name__ == '__main__':
    app.run(debug=True)
