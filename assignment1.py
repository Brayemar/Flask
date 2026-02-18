# create a route that is able to calculate the simple interest given the pricipal as 20000, rate as 7% and time as 8 years.
from flask import *
app = Flask(__name__)

@app.route("/api/multiply", methods=["POST"])
def multipy():
    if request.method == "POST":
        principal = request.form["principal"]
        rate = request.form["rate"]
        time = request.form["time"]
        divide = request.form["divide"]
        si = (int(principal) * int(rate) * int(time)) / int(divide)

        return jsonify({"The answer is " : si})


# Below we run the application
app.run(debug=True)