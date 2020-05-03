from flask import make_response, render_template
import json
import pyodbc
from __main__ import connection
import model.product as product_queries
import model.seller as seller_queries
import model.classifier as classifier_queries
import model.warehouse as warehouse_queries
import model.supplier as supplier_queries
import script.sql_helper as sql_helper

def count_all():
	cursor = connection.cursor()
	total_classifiers_query = classifier_queries.count_total_classifiers
	total_products_query = product_queries.count_total_products
	total_sellers_query = seller_queries.count_total_sellers
	total_suppliers_query = supplier_queries.count_total_suppliers
	total_warehouses_query = warehouse_queries.count_total_warehouses
	response_data = []

	try:
		classifier_result = cursor.execute(total_classifiers_query)
		product_result = cursor.execute(total_products_query)
		seller_result = cursor.execute(total_sellers_query)
		supplier_result = cursor.execute(total_suppliers_query)
		warehouse_result = cursor.execute(total_warehouses_query)

		classifier_data = classifier_result.fetchall()
		product_data = product_result.fetchall()
		seller_data = seller_result.fetchall()
		supplier_data = supplier_result.fetchall()
		warehouse_data = warehouse_result.fetchall()

		classifier_columns = sql_helper.get_columns_from_result(classifier_result.description)
		product_columns = sql_helper.get_columns_from_result(product_result.description)
		seller_columns = sql_helper.get_columns_from_result(seller_result.description)
		supplier_columns = sql_helper.get_columns_from_result(supplier_result.description)
		warehouse_columns = sql_helper.get_columns_from_result(warehouse_result.description)

		classifier_response_data = sql_helper.sql_select_result_to_json(classifier_columns, classifier_data)
		product_response_data = sql_helper.sql_select_result_to_json(product_columns, product_data)
		seller_response_data = sql_helper.sql_select_result_to_json(seller_columns, seller_data)
		supplier_response_data = sql_helper.sql_select_result_to_json(supplier_columns, supplier_data)
		warehouse_response_data = sql_helper.sql_select_result_to_json(warehouse_columns, warehouse_data)

		print(classifier_response_data)
		print(product_response_data)
		print(seller_response_data)
		print(supplier_response_data)
		print(warehouse_response_data)
	except pyodbc.DatabaseError as error:
		raise error
		return make_response({ 'status': 'error', 'error': error }, 400)
	finally:
		if len(response_data) == 0:
			return make_response({ 'status': 'count_all_data_not_found', 'data': [] }, 404)
		else:
			return make_response(json.dumps({ 'status': 'count_all_data', 'data': { 'classifier': classifier_response_data, 'product': product_response_data, 'seller': seller_response_data, 'supplier': supplier_response_data, 'warehouse': warehouse_response_data } }, default = sql_helper.default), 200)

def home():
    # return make_response({ 'status': 'ok' }, 200)
    return render_template('app.html')
