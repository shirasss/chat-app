
from flask import Flask, render_template,Markup,request,redirect,url_for,session
import csv
import os
import base64
from enum import Enum
from flask_session import Session

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
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        status,msg = check_if_user_exists(username,password)
        if status == user_status.NO_MATCH.value:
           write_to_csv(username,password)
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
                if pws == password:
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
        # user_data = load_user_data()
        username = request.form['username']
        password = request.form['password']
        status,msg=check_if_user_exists(username,password)
        if status == user_status.PASS_AND_NAME_MATCH.value:
            session['user_name'] = username
            session['user_password'] = password
            return redirect("/lobby") 
        # if username in user_data:
        #     stored_password = user_data[username]
        #     if encode_password(password) == stored_password:
        #         # return render_template('lobby.html')
        #         return "in lobby"
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/lobby', methods=['GET'])
def lobby():
    # Display the main lobby page where users can create or enter chat rooms
    # return f"lobby{session.get('user_name')}"\
    return render_template('lobby.html')


@app.route('/logout', methods=['GET','POST'])
def logOut():
    session.pop('username', 'password')
    return redirect('login')

@app.route('/chat/<room>', methods=['GET','POST'])
def chat_room(room):
    # Display the specified chat room with all messages sent
    if request.method == 'POST':
        msg = request.form['msg']
        return msg
    else:
        return render_template('chat.html')

# @app.route('/lobby', methods=['GET'])
# def lobby():
#  # Display the main lobby page where users can create or enter chat rooms
#     create_a_room(request.json.get('new_room'))

# def create_a_room(room):
#     rooms = os.listdir('./rooms')
#     if room not in rooms:
#        room_file = open('${room}.txt', 'w')
#        room_file.write('first line')
#        room_file.close()
#        return redirect(url_for('/chat/${room}'))
#     else:
#        return redirect(url_for('/lobby'))



def encode_password(password):
    return base64.encode("Encode this text")

def decode_password(password):
    return base64.decode("Encode this text")

def load_user_data():
    user_data = {}
    with open('user.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            username = row[0]
            password = row[1]
            user_data[username] = password
    return user_data


if __name__ == '__main__':
   app.run(host="0.0.0.0")



# @app.route('/login', methods=['GET','POST'])
# def loginPage():
# #    if request.method == 'POST':
#         # username = request.form['username']
#         # userpass = request.form['password']
#         # user_exists = check_if_user_exists(username, userpass)
#         # if user_exists:
#         #     return render_template('login.html')
#    return render_template('login.html')


# ==============================================================





# from flask import Flask, render_template, request, redirect
# import csv
# from enum import Enum
# import base64

# class user_status(Enum):
#     PASS_AND_NAME_MATCH = 1
#     NAME_MATCH = 2
#     NO_MATCH = 3
#     ERROR = 4


# app = Flask("__name__")

# def encode_password(user_pass):
#     pass_bytes = user_pass.encode('ascii')
#     base64_bytes = base64.b64encode(pass_bytes)
#     base64_message = base64_bytes.decode('ascii')
#     return base64_message

# def decode_password(user_pass):
#     base64_bytes = user_pass.encode('ascii')
#     pass_bytes = base64.b64decode(base64_bytes)
#     user_pass = pass_bytes.decode('ascii')
#     return user_pass

# def add_user_to_csv(username, userpass):
#     f = open('users.csv', 'a')
#     writer = csv.writer(f)
#     writer.writerow([username,userpass])
#     f.close()

# def check_if_user_exists(username, userpass):
#     with open('users.csv', 'r') as users:
#         users_arr = csv.reader(users)
#         for user in users_arr:
#             if user[0] == username:
#                 if user[1] != userpass:
#                      msg = "user with that name already exist"
#                      status = 1
#                 else:
#                      msg = "you already registered, please login"
#                      status = 2
#                 return status, msg
#         return 3, " "
#     return 4, "ERROR"


# @app.route('/', methods=['GET','POST'])
# def homePage():
#     msg = " "
#     if request.method == 'POST':
#         username = request.form['username']
#         userpass = request.form['password']
#         status, msg = check_if_user_exists(username, userpass)
#         if status == user_status.NO_MATCH.value :
#             add_user_to_csv(username, userpass)
#             return redirect('/login')
#         elif status == user_status.NAME_MATCH.value:
#            return render_template("login.html")
#     return render_template("register.html")
# @app.route('/login', methods=['GET','POST'])
# def loginPage():
#    if request.method == 'POST':
#         username = request.form['username']
#         userpass = request.form['password']
#         user_exists, msg = check_if_user_exists(username, userpass)
#         if user_exists:
#             return render_template('login.html')
#    return render_template('login.html')

