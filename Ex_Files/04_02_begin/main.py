from flask import Flask

app = Flask(__name__)

@app.route("/") #adding a decorator for the route
def hello():
    return "Hello, World"

app.run(debug=True)
