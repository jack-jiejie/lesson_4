__author__ = "yin"
__data__ = "2020/4/9 13:14"


from flask import Flask, make_response

app = Flask(__name__)

# 路由，访问路径
@app.route('/hello')
def hello_world():

    headers = {
        'content-type': 'text/plain'
    }
    response = make_response("<html>sadwf</html>")
    response.headers = headers
    return response
@app.route('/getjson')
def get_json():
    headers = {
        'content-type': 'text/plain'
    }
    result = {
        "name": "yinzhangjie",
        "age": 18
    }
    response = make_response(str(result))
    response.headers = headers
    return response
app.config.from_object('config')
app.run(host='0.0.0.0', debug=app.config["DEBUG"])




