from flask import make_response, render_template
import json
import pyodbc
from __main__ import connection
import model.aggregate as aggregate_queries
import script.sql_helper as sql_helper

def count_all():
	cursor = connection.cursor()

	try:
		classifier_result = cursor.execute(aggregate_queries.count_total)
		classifier_data = classifier_result.fetchall()
		classifier_columns = sql_helper.get_columns_from_result(classifier_result.description)
		classifier_response_data = sql_helper.sql_select_result_to_json(classifier_columns, classifier_data)
	except pyodbc.DatabaseError as error:
		raise error
		return make_response({ 'status': 'error', 'error': error }, 400)
	finally:
		if len(classifier_response_data) == 0:
			return make_response({ 'status': 'aggregate_count_not_found', 'data': [] }, 404)
		else:
			return make_response({ 'status': 'count_found', 'data': classifier_response_data }, 200)

def home():
    # return make_response({ 'status': 'ok' }, 200)
    return render_template('app.html')
