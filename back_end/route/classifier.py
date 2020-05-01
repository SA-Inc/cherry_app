from flask import Blueprint, request
import controller.classifier

classifier = Blueprint('classifier', __name__)

@classifier.route('/create', methods = ['POST'])
def create_classifier():
    data = request.get_json()
    return controller.classifier.create_classifier(data)

@classifier.route('/read_all', methods = ['GET'])
def read_all_classifiers():
    return controller.classifier.read_all_classifiers()

@classifier.route('/read/<code>', methods = ['GET'])
def read_classifier(code):
    return controller.classifier.read_classifier(code)

@classifier.route('/update/<code>', methods = ['PUT'])
def update_classifier(code):
    data = request.get_json()
    return controller.classifier.update_classifier(code, data)

@classifier.route('/delete/<code>', methods = ['DELETE'])
def delete_classifier(code):
    return controller.classifier.delete_classifier(code)
