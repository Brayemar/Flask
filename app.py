# import the flask framework
from flask import *


# Below we create a web serverbased application
app = Flask(__name__)

# below we create the home route.
# Routing: This is mapping/connecting different functions. We do this by the help of a decorator
@app.route("/api/home")
def home():
    return jsonify({"message" : "Home Route accessed"})


# Below is the products route
@app.route("/api/products")
def products():
    return jsonify({"message" : "Welcome to the products route"})


# Below is a route for addition
@app.route("/api/calc", methods=["POST"])
def calculator():
    if request.method == "POST":
        number1 = request.form["number1"]
        number2 = request.form["number2"]
        sum = int(number1) + int(number2)

        return jsonify({"The answer is " : sum})


# Below we run the application
app.run(debug=True)

# create a route that is able to calculate the simple interest given the pricipal as 20000, rate as 7% and time as 8 years.