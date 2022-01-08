from flask import Flask, request
from dbmanager import addNewProduct, getProducts, delProduct, updateProduct
from werkzeug.exceptions import HTTPException
import json

app = Flask("Shop")

@app.route('/products/<int:product_id>', methods=["GET"])
def listProducts(product_id):
    try:
        return {"product": getProducts(product_id)}, 200
    except Exception as e:
        handleException

@app.route("/addproduct", methods=["POST"])
def newProduct():
    try:
        body = request.get_json()
        id = addNewProduct(body['name'], body['section'], body['price'], body['available'])
        return {"product_id": id}, 200
    except Exception as e:
        handleException

@app.route("/products/edit/<int:product_id>", methods=["PUT"])
def editProduct(product_id):
    try:
        body = request.get_json()
        updateProduct(product_id, body)
        return {"product": getProducts(product_id)},200
    except Exception as e:
        handleException 

@app.route("/delproduct", methods=["DELETE"])
def deleteProduct():
    try:
        body = request.get_json()
        product = getProducts(body['id'])
        delProduct(body['id'])
        return {"product": product}, 200
    except Exception as e:
        handleException

@app.errorhandler(HTTPException)
def handleException(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response
app.run()