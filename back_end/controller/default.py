from flask import make_response

def home():
    return make_response({ 'status': 'ok' }, 200)
