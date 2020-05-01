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

@product.route('/read/<id>', methods = ['GET'])
def read_product(id):
    return controller.product.read_product(id)

@product.route('/update/<id>', methods = ['PUT'])
def update_product(id):
    data = request.get_json()
    return controller.product.update_product(id, data)

@product.route('/delete/<id>', methods = ['DELETE'])
def delete_product(id):
    return controller.product.delete_product(id)
