from flask import Blueprint

app = Blueprint('api', __name__)

@app.route('/api/hello')
def hello():
    return "api_hello"