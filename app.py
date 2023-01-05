from flask import Flask, request, jsonify
from flask_cors import CORS # 允许跨域访问
from db import get_db

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
    print('into query')
    if request.method == 'GET':
        # 获取数据
        print(request.form)
        # 数据验证
        # 执行数据库操作
        #db = get_db()
        return 'response answer'


if __name__ == "__main__":
    app.run(port=5001, debug=True)