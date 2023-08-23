# from flask import Flask
# server = Flask(__name__)
# @server.route("/")
# def hello():
#     return "hello world$$$$"
# if __name__ == "__main__":
#     server.run(host="0.0.0.0")




from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('lobby.html')
if __name__ == '__main__':
   app.run(host="0.0.0.0")