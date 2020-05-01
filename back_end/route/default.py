from flask import Blueprint
import controller.default

default = Blueprint('default', __name__)

@default.route('/', methods = ['GET'])
def home():
    return controller.default.home()
