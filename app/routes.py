from flask import jsonify, request
import json
from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/question/<int:level>', methods=['GET'])
def question(level:int):
    """
    GET request to get a question for the user based on their current level
    """
    f=open("./gameinfo.json", "r")
    qn = json.load(f)["questions"][level-1]

    if request.method == 'GET':
        qns = {
            "Level": level,
            "type":qn["type"],
            "question": qn["question"],
            "options":qn["options"],
            "answer": qn["answer"],
            "xpOnSuccess":  qn["xpOnSuccess"],
        }
    
    return jsonify(qns)
    
