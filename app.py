# Framework de python para levantar el servidor, en este caso vamos a usar Flask.
# Request, proporcionar los datos que me envian a traves de  http

from flask import Flask, jsonify, request

app =  Flask(__name__)


from products import products

# probar las peticiones 

@app.route('/hello')    
def world():
    return jsonify({"hello" : "world"})

#Get all

@app.route('/products')
def getProducts():
    return jsonify({"Mensaje": "list of products ", "products": products})
#Get 
@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) >0):
        return jsonify({"product" : productsFound[0]})
    return 'Product not found'

# PUT
@app.route('/products', methods = ['POST'])
def addProduct():
    newProduct = {
        "name" : request.json['name'],
        "price": request.json['price'],
        "quantity" :  request.json['quantity']
    }
    products.append(newProduct)
    return jsonify({"message": "Added ok", "products" : products})

# EDIT 
@app.route('/products/<string:product_name>', methods = ['PUT'])
def editProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
       productsFound[0]['name'] = request.json['name']
       productsFound[0]['price'] = request.json['price']
       productsFound[0]['quantity'] = request.json['quantity']
       
       return jsonify({
           "message" : "product update",
           "product" : productsFound[0]
       })

    return jsonify({"message" : "product not found"})

#DELETE

@app.route('/products/<string:product_name>', methods = ['DELETE'])
def deleteProduct(product_name):
     productsFound = [product for product in products if product['name'] == product_name]
     if (len(productsFound) > 0):
         products.remove(productsFound[0])
         return jsonify({
             "message" : "Product deleted",
             "products": products
         })

     return jsonify({"message" : "product not found"})


if __name__ == '__main__':
    app.run(debug=True, port=5000)

