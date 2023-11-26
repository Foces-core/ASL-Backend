from flask import jsonify, request
from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/question/<level>', methods=['GET'])
def question(level: int):
    """
    GET request to get a question for the user based on their current level
    """
    
    qns = {}
    if request.method == 'GET':
        qns = {
            "question": None,
            "options": None,
            "optionCount":None,
            "xpOnSuccess": None,
        }

    return jsonify(qns)
    
