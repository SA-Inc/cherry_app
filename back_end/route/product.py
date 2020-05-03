from flask import Blueprint, request
import controller.product

product = Blueprint('product', __name__)

@product.route('/create', methods = ['POST'])
def create_product():
    data = request.get_json()
    return controller.product.create_product(data)

@product.route('/read_all', methods = ['GET'])
def read_all_products():
    return controller.product.read_all_products()

@product.route('/read/<id_prod>', methods = ['GET'])
def read_product(id_prod):
    return controller.product.read_product(id_prod)

@product.route('/update/<id_prod>', methods = ['PUT'])
def update_product(id_prod):
    data = request.get_json()
    return controller.product.update_product(id_prod, data)

@product.route('/delete/<id_prod>', methods = ['DELETE'])
def delete_product(id_prod):
    return controller.product.delete_product(id_prod)
