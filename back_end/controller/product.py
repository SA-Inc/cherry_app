import json
from flask import make_response
import pyodbc
from __main__ import connection
import model.product as product_queries
import script.sql_helper as sql_helper



def create_product(data):
	cursor = connection.cursor()
	query = product_queries.insert_product
	data = (data['name'], data['description'], data['price'])

	try:
		cursor.execute(query, data)
	except pyodbc.DatabaseError as error:
		raise error
		cursor.rollback()
		return make_response({ 'error': error }, 400)
	finally:
		cursor.commit()

		return make_response({ 'result': True }, 201)



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
		return make_response({ 'error': error }, 400)
	finally:
		if len(response_data) == 0:
			return make_response({ 'data': None }, 404)
		else:
			return make_response({ 'data': response_data }, 200)



def read_product(id):
	cursor = connection.cursor()
	query = product_queries.select_product_by_id
	response_data = []

	try:
		result = cursor.execute(query, id)
		data = result.fetchall()
		columns = sql_helper.get_columns_from_result(result.description)
		response_data = sql_helper.sql_select_result_to_json(columns, data)
	except pyodbc.DatabaseError as error:
		raise error
		return make_response({ 'error': error }, 400)
	finally:
		if len(response_data) == 0:
			return make_response({ 'data': None }, 404)
		else:
			return make_response({ 'data': response_data }, 200)



def update_product(id, data):
	cursor = connection.cursor()
	query = product_queries.update_product_by_id
	data = (data['name'], data['description'], data['price'], id)

	try:
		result = cursor.execute(query, data)
	except pyodbc.DatabaseError as error:
		raise error
		cursor.rollback()
		return make_response({ 'error': error }, 400)
	finally:
		cursor.commit()

		if cursor.rowcount == -1 or cursor.rowcount == 0:
			return make_response({ 'result': False }, 404)
		else:
			return make_response({ 'result': True }, 200)



def delete_product(id):
	cursor = connection.cursor()
	query = product_queries.delete_product_by_id

	try:
		result = cursor.execute(query, id)
	except pyodbc.DatabaseError as error:
		raise error
		cursor.rollback()
		return make_response({ 'error': error }, 400)
	finally:
		cursor.commit()

		if cursor.rowcount == 0:
			return make_response({ 'result': False }, 404)
		else:
			return make_response({ 'result': True }, 200)
