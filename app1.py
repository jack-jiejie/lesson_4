__author__ = "yin"
__data__ = "2020/4/9 13:14"

from flask import Flask, make_response, jsonify

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

@app.route("/getjson3")
def get_json3():
    result = {
        "name": "yinzhangjie",
        "age": 18
    }
    return jsonify(result)
@app.route("/param/<d1>/<d2>")
def param(d1, d2):
    print(d1)
    print(d2)
    return "1"

app.config.from_object('config')
app.run(debug=app.config["DEBUG"], port=5001)
# app.run(debug=True, port=5001)