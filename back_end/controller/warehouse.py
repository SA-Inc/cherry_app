import json
from flask import make_response
import pyodbc
from __main__ import connection
import model.warehouse as warehouse_queries
import script.sql_helper as sql_helper

def create_warehouse(data):
  cursor = connection.cursor()
  query = warehouse_queries.insert_warehouse
  data = (data['code'], data['supplier'], data['receipt_date'], data['value_product'], data['price'], data['first_value'])

  print(data)
  try:
    cursor.execute(query, data)
  except pyodbc.DatabaseError as error:
    raise error
    cursor.rollback()
    return make_response({ 'status': 'error', 'error': error }, 400)
  finally:
    cursor.commit()
    return make_response({ 'status': 'warehouse_was_created', 'data': {} }, 200)



def read_all_warehouses():
  cursor = connection.cursor()
  query = warehouse_queries.select_all_warehouses
  response_data = []

  try:
    result = cursor.execute(query)
    data = result.fetchall()
    columns = sql_helper.get_columns_from_result(result.description)
    response_data = sql_helper.sql_select_result_to_json(columns, data)

  except pyodbc.DatabaseError as error:
    raise error
    return make_response({ 'status': 'error', 'error': error }, 400)
  finally:
    if len(response_data) == 0:
      return make_response({ 'status': 'warehouses_not_found', 'data': [] }, 404)
    else:
      return make_response(json.dumps({ 'status': 'warehouses_found', 'data': response_data }, default = sql_helper.default), 200)



def read_warehouse(id_wh):
  cursor = connection.cursor()
  query = warehouse_queries.select_warehouse_by_id
  response_data = {}

  try:
    result = cursor.execute(query, id_wh)
    data = result.fetchall()
    columns = sql_helper.get_columns_from_result(result.description)
    response_data = sql_helper.sql_select_result_to_json(columns, data)
  except pyodbc.DatabaseError as error:
    raise error
    return make_response({ 'status': 'error', 'error': error }, 400)
  finally:
    if len(response_data) == 0:
      return make_response({ 'status': 'warehouse_not_found', 'data': {} }, 404)
    else:
      return make_response(json.dumps({ 'status': 'warehouse_found', 'data': response_data }, default = sql_helper.default), 200)



def read_warehouse_id():
  cursor = connection.cursor()
  query = warehouse_queries.select_warehouse_id
  response_data = []

  try:
    result = cursor.execute(query)
    data = result.fetchall()
    columns = sql_helper.get_columns_from_result(result.description)
    response_data = sql_helper.sql_select_result_to_json(columns, data)
  except pyodbc.DatabaseError as error:
    raise error
    return make_response({ 'status': 'error', 'error': error }, 400)
  finally:
    if len(response_data) == 0:
      return make_response({ 'status': 'warehouse_not_found', 'data': [] }, 404)
    else:
      return make_response({ 'status': 'warehouses_found', 'data': response_data }, 200)



def update_warehouse(id_wh, data):
  cursor = connection.cursor()
  query = warehouse_queries.update_warehouse_by_id
  data = (data['code'], data['supplier'], data['receipt_date'], data['value_product'], data['price'], data['first_value'], id_wh)

  try:
    result = cursor.execute(query, data)
  except pyodbc.DatabaseError as error:
    raise error
    cursor.rollback()
    return make_response({ 'status': 'error', 'error': error }, 400)
  finally:
    cursor.commit()

    if cursor.rowcount == -1 or cursor.rowcount == 0:
      return make_response({ 'status': 'warehouse_not_found', 'data': {} }, 404)
    else:
      return make_response({ 'status': 'warehouse_updated', 'data': {} }, 200)



def delete_warehouse(id_wh):
  cursor = connection.cursor()
  query = warehouse_queries.delete_warehouse_by_id

  try:
    result = cursor.execute(query, id_wh)

    cursor.commit()

    if cursor.rowcount == 0:
      return make_response({ 'status': 'warehouse_not_found', 'data': {} }, 404)
    else:
      return make_response({ 'status': 'warehouse_deleted', 'data': {} }, 200)
  except pyodbc.Error as error:
    cursor.rollback()
    error_code = error.args[0]

    if error_code == '23000':
      return make_response({ 'status': 'error', 'code': 23000, 'error': 'can_not_delete_foreign_key_conflict' }, 400)
    