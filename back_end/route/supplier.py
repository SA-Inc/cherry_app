from flask import Blueprint, request
import controller.supplier

supplier = Blueprint('supplier', __name__)

@supplier.route('/create', methods = ['POST'])
def create_supplier():
    data = request.get_json()
    return controller.supplier.create_supplier(data)

@supplier.route('/read_all', methods = ['GET'])
def read_all_suppliers():
    return controller.supplier.read_all_suppliers()

@supplier.route('/read/<id_sup>', methods = ['GET'])
def read_supplier(id_sup):
    return controller.supplier.read_supplier(id_sup)

@supplier.route('/update/<id_sup>', methods = ['PUT'])
def update_supplier(id_sup):
    data = request.get_json()
    return controller.supplier.update_supplier(id_sup, data)

@supplier.route('/delete/<id_sup>', methods = ['DELETE'])
def delete_supplier(id_sup):
    return controller.supplier.delete_supplier(id_sup)
