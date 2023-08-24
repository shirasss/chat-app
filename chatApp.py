from flask import Flask, render_template,Markup,request,redirect,url_for,session
import csv
import os
import base64
from enum import Enum
import datetime
from flask_session import Session
ROOMS=[]
class user_status(Enum):
    PASS_AND_NAME_MATCH = 1
    NAME_MATCH = 2
    NO_MATCH = 3
    ERROR = 4

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/',methods=['GET','POST'] )
def homePage():
    return redirect("/register") 
    

@app.route('/register',methods=['GET','POST'] )
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        status,msg = check_if_user_exists(username,password)
        if status == user_status.NO_MATCH.value:
           write_to_csv(username,encode_password(password))
           return redirect("/login")
        elif status == user_status.NAME_MATCH.value:
           return msg
        elif status == user_status.PASS_AND_NAME_MATCH.value:
            return redirect("/login") 
    else:
        return render_template('register.html')
    
def check_if_user_exists(username, password):
    filename = "user.csv"
    with open(filename, 'r',newline="") as file:
        csv_reader = csv.reader(file) 
        for row in csv_reader:
            name, pws= row[0],row[1] 
            if name == username:
                if decode_password(pws) == password:
                   return 1,"user and password are correct"
                else:
                    return 2,"User name already exists"
    return 3,"new user"


def write_to_csv(username,password):
    filename="user.csv"
    with open(filename,"a") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        status,msg=check_if_user_exists(username,password)
        if status == user_status.PASS_AND_NAME_MATCH.value:
            session['user_name'] = username
            session['user_password'] = password
            return redirect("/lobby") 
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/lobby', methods=['GET','POST'])
def lobby():#session
    if request.method == 'POST':
        create_a_room(request.form['new_room'])
    else:
        enter_room(request.args.get('room'))
    return render_template('lobby.html', room_names=ROOMS)

def create_a_room(room):
    if room not in ROOMS:
        #try:
            room_file = open('rooms/{}.txt'.format(room), 'w')
            room_file.write('Wellcom To {} room!'.format(room))
            room_file.close()
            ROOMS.append(room)
    else:
        print("The room name is already exist")
        

def enter_room(room):
    return render_template('chat.html',room=room)


@app.route('/logout', methods=['GET','POST'])
def logOut():
    session.pop('username', 'password')
    return redirect('login')

@app.route('/chat/<room>', methods=['GET','POST'])
def chat_room(room):
    # Display the specified chat room with all messages sent
    return render_template('chat.html',room=room)

@app.route('/api/chat/<room>', methods=['GET','POST'])
def add_msg(room):
    if request.method == 'POST':
        filename = "/rooms/"+room+".txt"
        msg = request.form['msg']
        if "user_name" in session:
            # Get the current date and time
            current_datetime = datetime.datetime.now()
            # Format the date and time as a string
            formatted_datetime = current_datetime.strftime("[%Y-%m-%d %H:%M:%S]")
            with open(filename,"a") as file:
                file.write(formatted_datetime+" "+session.get('user_name')+":"+msg)
    with open(filename,"r") as file:
        room_data = file.read()
        return room_data


def encode_password(password):
    pass_bytes = password.encode('ascii')
    base64_bytes = base64.b64encode(pass_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

def decode_password(password):
    base64_bytes = password.encode('ascii')
    pass_bytes = base64.b64decode(base64_bytes)
    password = pass_bytes.decode('ascii')
    return password

if __name__ == '__main__':
   app.run(host="0.0.0.0")

