from flask import Flask, request
from dbmanager import addNewProduct, listProducts, delProduct
import json

app = Flask("Shop")

@app.route("/products", methods=["GET"])
def getProducts():
    try:
        return {"products": listProducts()}, 200
    except Exception as e:
        response = app.get_response()
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response

@app.route('/products/<int:page_id>')
def getSpecificProduct(page_id):
    try:
        return {"product": listProducts(page_id)}, 200
    except Exception as e:
        response = app.get_response()
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response

@app.route("/addproduct", methods=["POST"])
def newProduct():
    try:
        body = request.get_json()
        addNewProduct(body['name'], body['section'], body['price'], body['available'])
        return 200
    except Exception as e:
        response = app.get_response()
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response

@app.route("/delproduct", methods=["DELETE"])
def deleteProduct():
    try:
        body = request.get_json()
        delProduct(body['id'])
        return 200
    except Exception as e:
        response = app.get_response()
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response

app.run()