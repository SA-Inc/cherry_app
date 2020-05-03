import json
from flask import make_response
import pyodbc
from __main__ import connection
import model.supplier as supplier_queries
import script.sql_helper as sql_helper

def create_supplier(data):
  cursor = connection.cursor()
  query = supplier_queries.insert_supplier
  data = (data['company_name'], data['bank'], data['account_number'], data['phone_number'], data['email'], data['id_wh'])

  try:
    cursor.execute(query, data)
  except pyodbc.DatabaseError as error:
    raise error
    cursor.rollback()
    return make_response({ 'status': 'error', 'error': error }, 400)
  finally:
    cursor.commit()
    return make_response({ 'status': 'supplier_was_created', 'data': {} }, 200)



def read_all_suppliers():
  cursor = connection.cursor()
  query = supplier_queries.select_all_suppliers
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
      return make_response({ 'status': 'suppliers_not_found', 'data': [] }, 404)
    else:
      return make_response({ 'status': 'suppliers_found', 'data': response_data }, 200)



def read_supplier(id_sup):
  cursor = connection.cursor()
  query = supplier_queries.select_supplier_by_id
  response_data = {}

  try:
    result = cursor.execute(query, id_sup)
    data = result.fetchall()
    columns = sql_helper.get_columns_from_result(result.description)
    response_data = sql_helper.sql_select_result_to_json(columns, data)
  except pyodbc.DatabaseError as error:
    raise error
    return make_response({ 'status': 'error', 'error': error }, 400)
  finally:
    if len(response_data) == 0:
      return make_response({ 'status': 'supplier_not_found', 'data': {} }, 404)
    else:
      return make_response({ 'status': 'suppliers_found', 'data': response_data }, 200)



def update_supplier(id_sup, data):
  cursor = connection.cursor()
  query = supplier_queries.update_supplier_by_id
  data = (data['company_name'], data['bank'], data['account_number'], data['phone_number'], data['email'], data['id_wh'], id_sup)

  try:
    result = cursor.execute(query, data)
  except pyodbc.DatabaseError as error:
    raise error
    cursor.rollback()
    return make_response({ 'status': 'error', 'error': error }, 400)
  finally:
    cursor.commit()

    if cursor.rowcount == -1 or cursor.rowcount == 0:
      return make_response({ 'status': 'supplier_not_found', 'data': {} }, 404)
    else:
      return make_response({ 'status': 'supplier_updated', 'data': {} }, 200)



def delete_supplier(id_sup):
  cursor = connection.cursor()
  query = supplier_queries.delete_supplier_by_id

  try:
    result = cursor.execute(query, id_sup)
  except pyodbc.DatabaseError as error:
    raise error
    cursor.rollback()
    return make_response({ 'status': 'error', 'error': error }, 400)
  finally:
    cursor.commit()

    if cursor.rowcount == 0:
      return make_response({ 'status': 'supplier_not_found', 'data': {} }, 404)
    else:
      return make_response({ 'status': 'supplier_deleted', 'data': {} }, 200)
