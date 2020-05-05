import json
from flask import make_response
import pyodbc
from __main__ import connection
import model.product as product_queries
import script.sql_helper as sql_helper



def create_product(data):
	cursor = connection.cursor()
	query = product_queries.insert_product
	data = (data['value_product'], data['date_sell'], data['price_prod'], data['id_sell'], data['id_wh'], data['code'])

	try:
		cursor.execute(query, data)
	except pyodbc.DatabaseError as error:
		raise error
		cursor.rollback()
		return make_response({ 'status': 'error', 'error': error }, 400)
	finally:
		cursor.commit()
		return make_response({ 'status': 'product_was_created', 'data': {} }, 200)



def read_all_products():
	cursor = connection.cursor()
	query = product_queries.select_all_products
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
			return make_response({ 'status': 'products_not_found', 'data': [] }, 404)
		else:
			return make_response(json.dumps({ 'status': 'products_found', 'data': response_data }, default = sql_helper.default), 200)



def read_product(id_prod):
	cursor = connection.cursor()
	query = product_queries.select_product_by_id
	response_data = []

	try:
		result = cursor.execute(query, id_prod)
		data = result.fetchall()
		columns = sql_helper.get_columns_from_result(result.description)
		response_data = sql_helper.sql_select_result_to_json(columns, data)
	except pyodbc.DatabaseError as error:
		raise error
		return make_response({ 'status': 'error', 'error': error }, 400)
	finally:
		if len(response_data) == 0:
			return make_response({ 'status': 'product_not_found', 'data': {} }, 404)
		else:
			return make_response(json.dumps({ 'status': 'product_found', 'data': response_data }, default = sql_helper.default), 200)



def update_product(id_prod, data):
	cursor = connection.cursor()
	query = product_queries.update_product_by_id
	data = (data['value_product'], data['date_sell'], data['price_prod'], data['id_sell'], data['id_wh'], data['code'], id_prod)

	try:
		result = cursor.execute(query, data)
	except pyodbc.DatabaseError as error:
		raise error
		cursor.rollback()
		return make_response({ 'status': 'error', 'error': error }, 400)
	finally:
		cursor.commit()

		if cursor.rowcount == -1 or cursor.rowcount == 0:
			return make_response({ 'status': 'product_not_found', 'data': {} }, 404)
		else:
			return make_response({ 'status': 'product_updated', 'data': {} }, 200)



# def delete_product(id_prod):
# 	cursor = connection.cursor()
# 	query = product_queries.delete_product_by_id

# 	try:
# 		result = cursor.execute(query, id_prod)
# 	except pyodbc.DatabaseError as error:
# 		raise error
# 		cursor.rollback()
# 		return make_response({ 'status': 'error', 'error': error }, 400)
# 	finally:
# 		cursor.commit()

# 		if cursor.rowcount == 0:
# 			return make_response({ 'status': 'product_not_found', 'data': {} }, 404)
# 		else:
# 			return make_response({ 'status': 'product_updated', 'data': {} }, 200)



def delete_product(id_prod):
  cursor = connection.cursor()
  query = product_queries.delete_product_by_id

  try:
    result = cursor.execute(query, id_prod)

    cursor.commit()

    if cursor.rowcount == 0:
      return make_response({ 'status': 'product_not_found', 'data': {} }, 404)
    else:
      return make_response({ 'status': 'product_deleted', 'data': {} }, 200)
  except pyodbc.Error as error:
    cursor.rollback()
    error_code = error.args[0]

    if error_code == '23000':
      return make_response({ 'status': 'error', 'code': 23000, 'error': 'can_not_delete_foreign_key_conflict' }, 400)
    else:
      return make_response({ 'status': 'error', 'error': 'unexpected_error' }, 400)
