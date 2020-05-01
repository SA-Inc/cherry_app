from flask import Flask, make_response
from flask_cors import CORS
import pyodbc

database_config = {
  'driver': '{ODBC Driver 17 for SQL Server}',
  'server': '',
  'database': '',
  'user': '',
  'password': ''
}

app = Flask(__name__)
CORS(app, resources = { r"/*": { "origins": "*" } })
connection = pyodbc.connect('DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password}'.format(**database_config))

cursor = connection.cursor()

# Check Connection to Database
cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()

from route.default import default
from route.error_handlers import error_handlers
from route.classifier import classifier
from route.warehouse import warehouse
from route.supplier import supplier
from route.seller import seller
from route.product import product

@app.errorhandler(404)
def not_found(error):
    return make_response({ 'status': 'not found' }, 404)

@app.errorhandler(405)
def method_not_found(error):
    return make_response({ 'status': 'method not allowed' }, 405)

@app.errorhandler(500)
def server_error(error):
    return make_response({ 'status': 'internal server error', 'error': error }, 500)

# Routes
app.register_blueprint(error_handlers)
app.register_blueprint(default, url_prefix = '/')
app.register_blueprint(classifier, url_prefix = '/api/classifier')
app.register_blueprint(warehouse, url_prefix = '/api/warehouse')
app.register_blueprint(supplier, url_prefix = '/api/supplier')
app.register_blueprint(seller, url_prefix = '/api/seller')
app.register_blueprint(product, url_prefix = '/api/product')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)
