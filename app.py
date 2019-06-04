import peewee
from flask import Flask, jsonify, request
from playhouse.shortcuts import model_to_dict


from models.produto import Product
from models.carrinho import Cart
from models.produtos_carrinho import Product_cart

app = Flask(__name__)

@app.route('/produtos')
def get_products():
    products = Product.select()
    list_products = []
    for product in products:
        list_products.append({
            'id': product.id,
            'name': product.name,
            'price': str(product.price)
        })
    return jsonify(list_products)

@app.route('/produtos', methods = ['POST'])
def post_products():
    data = request.get_json()
    product = Product.create(
        name = data.get('name'), 
        price = data.get('price')
    )
    return jsonify(model_to_dict(product))

@app.route('/carrinho', methods=['POST'])
def post_cart():
    data = request.get_json()
    cart = Cart.create(
        client_name = data.get('cliente')
    )
    return jsonify({'id': cart.id})

@app.route('/carrinho/<id>/produtos')
def get_cart(id):
    try:
        products = (
            Product_cart.select(Product.name, Product.price)
            .join(Product).where(Product_cart.cart_id==id).dicts()
        )
        sum_prod = 0
        list_products = []
        for product in products:
            sum_prod = sum_prod + product['price']
            list_products.append({
                'name': product['name'],
                'price': str(product['price'])
            })    
        total = sum_prod + len(list_products)
        return jsonify({
            'total': str(total),
            'items': list_products
        }), 200

    except Product_cart.DoesNotExist:
        return jsonify([]), 404

@app.route('/carrinho/<id>/produtos', methods=['POST'])
def post_cart_product(id):
    data = request.get_json()
    product_cart = Product_cart.create(
        cart_id = id,
        product_id = data.get('id_produto')
    )
    return jsonify([]), 201


if __name__ == '__main__':
    app.run(debug=True)