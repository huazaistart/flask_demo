from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    try:
        f = open('', 'w')
    except:
        pass
    # abort(404)
    return 'index'


@app.before_first_request
def before_first_request():
    print("在第一次请求之前被调用")


@app.before_request
def before_request():
    print("在每次请求之前被调用")


@app.after_request
def after_request(response):
    print("如果没有未处理的异常，在每次请求之后被调用")
    return response

@app.teardown_request
def teardown_request(e):
    print("在每次请求之后被调用，即使有未处理的异常")


if __name__ == '__main__':
    app.run(debug=True)