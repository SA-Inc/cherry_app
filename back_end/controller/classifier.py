import json
from flask import make_response
import pyodbc
from __main__ import connection
import model.classifier as classifier_queries
import script.sql_helper as sql_helper

def create_classifier(data):
  cursor = connection.cursor()
  query = classifier_queries.insert_classifier
  data = (data['code'],)

  print(data)

  try:
    cursor.execute(query, data)
  except pyodbc.DatabaseError as error:
    raise error
    cursor.rollback()
    return make_response({ 'status': 'error', 'error': error }, 400)
  finally:
    cursor.commit()
    return make_response({ 'status': 'classifier_was_created', 'data': {} }, 200)



def read_all_classifiers():
  cursor = connection.cursor()
  query = classifier_queries.select_all_classifiers
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
      return make_response({ 'status': 'classifers_not_found', 'data': [] }, 404)
    else:
      return make_response({ 'status': 'classifers_found', 'data': response_data }, 200)



def read_classifier(code):
  cursor = connection.cursor()
  query = classifier_queries.select_classifier_by_code
  response_data = {}

  try:
    result = cursor.execute(query, code)
    data = result.fetchall()
    columns = sql_helper.get_columns_from_result(result.description)
    response_data = sql_helper.sql_select_result_to_json(columns, data)
  except pyodbc.DatabaseError as error:
    raise error
    return make_response({ 'status': 'error', 'error': error }, 400)
  finally:
    if len(response_data) == 0:
      return make_response({ 'status': 'classifer_not_found', 'data': {} }, 404)
    else:
      return make_response({ 'status': 'classifers_found', 'data': response_data }, 200)



def update_classifier(code, data):
  cursor = connection.cursor()
  query = classifier_queries.update_classifier_by_code
  data = (data['code'], code)

  try:
    result = cursor.execute(query, data)
  except pyodbc.DatabaseError as error:
    raise error
    cursor.rollback()
    return make_response({ 'status': 'error', 'error': error }, 400)
  finally:
    cursor.commit()

    if cursor.rowcount == -1 or cursor.rowcount == 0:
      return make_response({ 'status': 'classifer_not_found', 'data': {} }, 404)
    else:
      return make_response({ 'status': 'classifers_updated', 'data': {} }, 200)



def delete_classifier(code):
  cursor = connection.cursor()
  query = classifier_queries.delete_classifier_by_code

  try:
    result = cursor.execute(query, code)
  except pyodbc.DatabaseError as error:
    raise error
    cursor.rollback()
    return make_response({ 'status': 'error', 'error': error }, 400)
  finally:
    cursor.commit()

    if cursor.rowcount == 0:
      return make_response({ 'status': 'classifer_not_found', 'data': {} }, 404)
    else:
      return make_response({ 'status': 'classifers_deleted', 'data': {} }, 200)
