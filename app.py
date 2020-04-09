__author__ = "yin"
__data__ = "2020/4/9 12:46"


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!aaabbb'
#
# if __name__ =="__main__":
#     app.run(debug=True)
#
# 通过配置文件载入的方法进行加载
app.config.from_object('config')
app.run(host='0.0.0.0', debug=app.config["DEBUG"], port=5001)
