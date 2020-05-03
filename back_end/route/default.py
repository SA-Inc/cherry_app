from flask import Blueprint
import controller.default

default = Blueprint('default', __name__)

@default.route('/', methods = ['GET'])
def home():
    return controller.default.home()

@default.route('/count', methods = ['GET'])
def count_all():
    return controller.default.count_all()
