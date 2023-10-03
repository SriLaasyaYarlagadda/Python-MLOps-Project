from flask import Flask

#We are creating an app object
app = Flask(__name__)

#We are creating app.route
@app.route("/")
#Now we are writing a function that returns "Hello World"
def index():
    return "Hello.World"

if __name__ == "_main_":
    app.run()
