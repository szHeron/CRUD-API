from flask import Flask, request
from dbmanager import addNewProduct, listProducts, delProduct

app = Flask("Shop")

@app.route("/products", methods=["GET"])
def getProducts():
    try:
        return {"products": listProducts()}
    except Exception as e:
        print(e)
        return {"error": e}

@app.route('/products/<int:page_id>')
def getSpecificProduct(page_id):
    try:
        return {"product": listProducts(page_id)}
    except Exception as e:
        print(e)
        return {"error": e}

@app.route("/addproduct", methods=["POST"])
def newProduct():
    try:
        body = request.get_json()
        addNewProduct(body['name'], body['section'], body['price'], body['available'])
        return {"success": True}
    except Exception as e:
        print(e)
        return {"success": False}

@app.route("/delproduct", methods=["DELETE"])
def deleteProduct():
    try:
        body = request.get_json()
        delProduct(body['id'])
        return {"success": True}
    except Exception as e:
        print(e)
        return {"success": False}

app.run()