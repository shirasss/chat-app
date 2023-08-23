
from flask import Flask, render_template
import base64
from tkinter import messagebox
import os

app = Flask(__name__)
 
@app.route('/')
def homePage():
    return Flask.redirect(url_for('/register'))

@app.route('/register', methods=['POST'])
def homePage():
    # Handle user login
    # Validate user credentials and generate a session token 
    pass


@app.route('/lobby', methods=['GET'])
def lobby():
    # Display the main lobby page where users can create or enter chat rooms
    create_a_room(request.json.get('new_room'))
    pass

def create_a_room(room):
    rooms = os.listdir('./rooms')
    if room not in rooms:
        room_file = open('${room}.txt', 'w')
        room_file.write('first line')###########
        room_file.close()
        return redirect(url_for('/chat/${room}'))
    else:
        return redirect(url_for('/lobby'))
        


@app.route('/chat/<room>', methods=['GET'])
def chat_room(room):
    # Display the specified chat room with all messages sent
    pass


@app.route('/login', methods=['POST'])
def loginPage():
    user_data = load_user_data()
    username = request.json.get('username')
    password = request.json.get('password')

    if username in user_data:
        stored_password = user_data[username]
        
        if encode_password(password) == stored_password:
            return redirect(url_for('/lobby'))
        else:
            return redirect(url_for('/login'))
    else:
        return redirect(url_for('/login'))

def encode_password(password):
    return base64.encode("Encode this text")

def decode_password(password):
    return base64.decode("Encode this text")

def load_user_data():
    user_data = {}
    with open('user_data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            username = row[0]
            password = row[1]
            user_data[username] = password
    return user_data


# Main function to run the application
if __name__ == '__main__':
   app.run(host="0.0.0.0")


@app.route('/logout', methods=['POST'])
def logOut():
    session.pop('username', 'password')
    messagebox.showinfo('Logout successfull') #alert
    return Flask.redirect(url_for('login'))

