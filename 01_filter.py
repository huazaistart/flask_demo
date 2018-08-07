from flask import Flask, render_template, request,current_app,g, session

app = Flask(__name__)

# 使用应用上下文时候，先要激活当前程序上下文，收回则是pop()
app.app_context().push()
print(current_app)
# print(request)
print(g)
# print(session)

# # 在设置session数据时候，需要配置secret_key对数据进行加密
app.config['SECRET_KEY'] = 'asdfghjkl'


@app.route('/')
def index():
    print(request)
    print(session)
    session["name"] = '冼秋华'
    # # session的数据赋给g变量，就不用每次调用都获取了
    # g.name = session.get("name")
    return render_template('01_filter.html')


@app.route('/g_name')
def g_name():
    # print(g.name)
    # print(session.get("name"))
    return 'fanche'

if __name__ == '__main__':
    app.run()
