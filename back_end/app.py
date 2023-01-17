# coding=utf-8
from flask import Flask, request, jsonify
from flask_cors import CORS # 允许跨域访问

from handler import query_handler

app = Flask(__name__)
CORS(app)

def get_guery():
    pass

@app.route('/')
def index():
    return 'server running'

# 返回数据即可
@app.route('/query', methods=['GET', 'POST'])
def query():
    if request.method == 'POST':
        # 当使用Ajax传递，post的数据其实是一个FormData
        # question = request.form["question"]
        # axios则是一个PayLoad
        question = request.get_json()["question"]
        return query_handler(question)


if __name__ == "__main__":
    app.run(port=5001, debug=True)