from flask import *
import os
import pymysql

app = Flask(__name__)

@app.route("/api/smartphones", methods=["POST"])
def smartphones():
    name = request.form["name"]
    brand = request.form["brand"]
    model = request.form["model"]
    storage = request.form["storage"]
    ram = request.form["ram"]
    battery = request.form["battery"]
    price = request.form["price"]
    stock = request.form["stock"]
    photo = request.files["photo"]

    # Save image
    filename = photo.filename
    photo.save(os.path.join("static/images", filename))

    # Connect to database
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",   # add your password
        database="online"
    )

    cursor = connection.cursor()

    sql = """
    INSERT INTO smartphones
    (name, brand, model, storage, ram, battery, price, stock, photo)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    data = (name, brand, model, storage, ram, battery, price, stock, filename)

    cursor.execute(sql, data)
    connection.commit()

    return jsonify({"message": "Product added successfully"})



# LAPTOPS API
@app.route("/api/laptops", methods=["POST"])
def laptops():
    name = request.form["name"]
    brand = request.form["brand"]
    processor = request.form["processor"]
    ram = request.form["ram"]
    storage = request.form["storage"]
    screensize = request.form["screensize"]
    price = request.form["price"]
    stock = request.form["stock"]
    photo = request.files["photo"]

    # Save image
    filename = photo.filename
    photo.save(os.path.join("static/images", filename))

    # Connect to database
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",   # add your password
        database="online"
    )

    cursor = connection.cursor()

    sql = """
    INSERT INTO laptops
    (name, brand, processor, ram, storage, screensize, price, stock, photo)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    data = (name, brand, processor, ram, storage, screensize, price, stock, filename)

    cursor.execute(sql, data)
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Product added successfully"})
    

app.run(debug=True)


app.run(debug=True)