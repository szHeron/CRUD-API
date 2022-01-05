from flask import Flask, request
from dbmanager import addNewProduct, listProducts

app = Flask("Shop")

@app.route("/products", methods=["GET"])
def getProducts():
    return {"products": listProducts()}

@app.route("/addproduct", methods=["POST"])
def newProduct():
    try:
        body = request.get_json()
        addNewProduct(body['name'], body['section'], body['price'], body['available'])
        return {"success": True}
    except:
        return {"success": False}
app.run()