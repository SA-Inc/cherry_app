import json
from flask import make_response
import pyodbc
from __main__ import connection
import model.seller as seller_queries
import script.sql_helper as sql_helper

def create_seller(data):
  cursor = connection.cursor()
  query = seller_queries.insert_seller
  data = (data['code'], data['supplier'], data['receipt_date'], data['value_product'], data['price'], data['first_value'])

  try:
    cursor.execute(query, data)
  except pyodbc.DatabaseError as error:
    raise error
    cursor.rollback()
    return make_response({ 'status': 'error', 'error': error }, 400)
  finally:
    cursor.commit()
    return make_response({ 'status': 'seller_was_created', 'data': {} }, 200)



def read_all_sellers():
  cursor = connection.cursor()
  query = seller_queries.select_all_sellers
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
      return make_response({ 'status': 'sellers_not_found', 'data': [] }, 404)
    else:
      return make_response({ 'status': 'sellers_found', 'data': response_data }, 200)



def read_seller(id_wh):
  cursor = connection.cursor()
  query = seller_queries.select_seller_by_id
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
      return make_response({ 'status': 'seller_not_found', 'data': {} }, 404)
    else:
      return make_response({ 'status': 'sellers_found', 'data': response_data }, 200)



def read_seller_id():
  cursor = connection.cursor()
  query = seller_queries.select_seller_id
  response_data = []

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
      return make_response({ 'status': 'seller_not_found', 'data': [] }, 404)
    else:
      return make_response({ 'status': 'sellers_found', 'data': response_data }, 200)



def update_seller(id_wh, data):
  cursor = connection.cursor()
  query = seller_queries.update_seller_by_id
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
      return make_response({ 'status': 'seller_not_found', 'data': {} }, 404)
    else:
      return make_response({ 'status': 'sellers_updated', 'data': {} }, 200)



def delete_seller(id_wh):
  cursor = connection.cursor()
  query = seller_queries.delete_seller_by_id

  try:
    result = cursor.execute(query, id_wh)
  except pyodbc.DatabaseError as error:
    raise error
    cursor.rollback()
    return make_response({ 'status': 'error', 'error': error }, 400)
  finally:
    cursor.commit()

    if cursor.rowcount == 0:
      return make_response({ 'status': 'seller_not_found', 'data': {} }, 404)
    else:
      return make_response({ 'status': 'sellers_deleted', 'data': {} }, 200)
