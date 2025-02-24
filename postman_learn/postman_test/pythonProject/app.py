# app.py
from flask import Flask, jsonify, request, abort
import json
import os

app = Flask(__name__)

# 初始化用户数据
with open('data/users.json', 'w') as f:
    json.dump([{"id": 1, "name": "John"}, {"id": 2, "name": "Alice"}], f)

@app.route('/')
def home():
    return "Welcome to Postman Practice API"

# 获取所有用户（GET）
# @app.route('/api/users', methods=['GET'])
# def get_users():
#     with open('data/users.json', 'r') as f:
#         users = json.load(f)
#     return jsonify(users)

# 创建用户（POST）
@app.route('/api/users', methods=['POST'])
def create_user():
    new_user = request.json
    with open('data/users.json', 'r+') as f:
        users = json.load(f)
        new_id = max(u['id'] for u in users) + 1
        new_user['id'] = new_id
        users.append(new_user)
        f.seek(0)
        json.dump(users, f)
    return jsonify(new_user), 201

# 获取单个用户（路径参数）
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    with open('data/users.json', 'r') as f:
        users = json.load(f)
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        abort(404)
    return jsonify(user)


if __name__ == '__main__':
    app.run()
