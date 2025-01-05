from flask import Flask, request, jsonify

app = Flask(__name__)

# 模拟的用户数据库
users = {
    "1": {"name": "Alice", "age": 25},
    "2": {"name": "Bob", "age": 30},
    "3": {"name": "Charlie", "age": 35}
}


@app.route('/user', methods=['GET'])
def get_user():
    # 获取查询参数中的用户 ID
    user_id = request.args.get('id')

    # 检查用户是否存在
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400  # 返回错误信息，状态码 400

    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404  # 返回错误信息，状态码 404

    # 返回用户信息
    return jsonify({"user": user}), 200  # 返回 JSON 数据和状态码 200


if __name__ == "__main__":
    app.run(debug=True)
