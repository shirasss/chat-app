
from flask import Flask, render_template,Markup,request,redirect,url_for
import csv

app = Flask(__name__)
 
@app.route('/',methods=['GET','POST'] )
def homePage():
    if request.method == 'POST':
       username = request.form['username']
       password = request.form['password']
       return check_if_user_exists(username,password)
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
                   return redirect('/login')
                else:
                    return "User name already exists"
    
    with open(filename,"a") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
        return redirect('/login') 
# def check_if_user_exist(username,password):
#     filename = "users.csv"
#     with open(filename, 'r') as file:
#         # creating a csv reader object
#         lines = csv.reader(file,delimiter="\n")
#         for line in lines:
#              name,pws=line[0].split(",")
#              if name == username:
#                  if pws!=password:
#                     return "user name alreadt exists"

@app.route('/login', methods=['GET','POST'])
def loginPage():
#    if request.method == 'POST':
        # username = request.form['username']
        # userpass = request.form['password']
        # user_exists = check_if_user_exists(username, userpass)
        # if user_exists:
        #     return render_template('login.html')
   return render_template('login.html')


# @app.route('/login', methods=['POST'])
# def loginPage():
#     # Handle user login
#     # Validate user credentials and generate a session token
#     return render_template('login.html')



# @app.route('/lobby', methods=['GET'])
# def lobby():
#     # Display the main lobby page where users can create or enter chat rooms
#     pass

# @app.route('/chat/<room>', methods=['GET'])
# def chat_room(room):
#     # Display the specified chat room with all messages sent
#     pass


# # Main function to run the application
if __name__ == '__main__':
   app.run(host="0.0.0.0")




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
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
#     app.debug = True

