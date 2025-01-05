from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 假设我们有一个简单的用户名和密码
USER_CREDENTIALS = {
    "username": "testuser",
    "password": "testpass"
}


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == USER_CREDENTIALS["username"] and password == USER_CREDENTIALS["password"]:
        return redirect(url_for('dashboard'))
    else:
        return "Login Failed! Invalid credentials.", 403


@app.route('/dashboard')
def dashboard():
    return "Welcome to the Dashboard!"


if __name__ == '__main__':
    app.run(debug=True)
