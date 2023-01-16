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

@app.route('/intro')
def intro():
    pass

# 返回数据即可
@app.route('/query', methods=['GET', 'POST'])
def query():
    if request.method == 'POST':
        question = request.form["question"]
        return query_handler(question)


if __name__ == "__main__":
    app.run(port=5001, debug=True)