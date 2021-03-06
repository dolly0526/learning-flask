from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login/')
def login():
    return '这是登录页面'

@app.route('/profile/')
def profile():
    # http://127.0.0.1:5000/profile/?name=dolly
    if request.args.get('name'):
        return '个人中心页面'
    # http://127.0.0.1:5000/profile
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()
