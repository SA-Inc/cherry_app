from flask import Blueprint, request
import controller.warehouse

warehouse = Blueprint('warehouse', __name__)

@warehouse.route('/create', methods = ['POST'])
def create_warehouse():
    data = request.get_json()
    return controller.warehouse.create_warehouse(data)

@warehouse.route('/read_all', methods = ['GET'])
def read_all_warehouses():
    return controller.warehouse.read_all_warehouses()

@warehouse.route('/read/<id_wh>', methods = ['GET'])
def read_warehouse(id_wh):
    return controller.warehouse.read_warehouse(id_wh)

@warehouse.route('/read_ids', methods = ['GET'])
def read_warehouse_id():
    return controller.warehouse.read_warehouse_id()

# @warehouse.route('/read/<id_wh>', methods = ['GET'])
# def read_warehouse(id_wh):
#     return controller.warehouse.read_warehouse(id_wh)

@warehouse.route('/update/<id_wh>', methods = ['PUT'])
def update_warehouse(id_wh):
    data = request.get_json()
    return controller.warehouse.update_warehouse(id_wh, data)

@warehouse.route('/delete/<id_wh>', methods = ['DELETE'])
def delete_warehouse(id_wh):
    return controller.warehouse.delete_warehouse(id_wh)
