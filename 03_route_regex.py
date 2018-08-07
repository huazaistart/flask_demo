from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 自定义正则转换器
class Regex(BaseConverter):
    def __init__(self, url, *args):
        super(Regex, self).__init__(url)
        # 接收第一个参数作为匹配规则
        self.regex = args[0]

# 将自定义正则转换器添加到url_map转换器中，并指定使用时的名字为re
app.url_map.converters["re"] = Regex


# 使用自定义正则转换器装饰视图函数
@app.route('/user/<re("[0-9]{3}"):id>')
def user_info(id):
    return "这是自定义正则转换器，接收到的参数为： %s" % id


if __name__ == '__main__':
    app.run()