from flask import Blueprint, request
import controller.seller

seller = Blueprint('seller', __name__)

@seller.route('/create', methods = ['POST'])
def create_seller():
    data = request.get_json()
    return controller.seller.create_seller(data)

@seller.route('/read_all', methods = ['GET'])
def read_all_sellers():
    return controller.seller.read_all_sellers()

@seller.route('/read/<id_sell>', methods = ['GET'])
def read_seller(id_sell):
    return controller.seller.read_seller(id_sell)

@seller.route('/read_ids', methods = ['GET'])
def read_seller_id():
    return controller.seller.read_seller_id()

@seller.route('/update/<id_sell>', methods = ['PUT'])
def update_seller(id_sell):
    data = request.get_json()
    return controller.seller.update_seller(id_sell, data)

@seller.route('/delete/<id_sell>', methods = ['DELETE'])
def delete_seller(id_sell):
    return controller.seller.delete_seller(id_sell)
