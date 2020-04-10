__author__ = "yzj"
__data__ = "2020/4/10 22:47"



from flask import jsonify, Blueprint, request

# 实例化蓝图对象
# user = Blueprint('web', __name__)
from . import api
@api.route("/users")
def users():
    result = {
        "computer": 131314,
        "brand": 1243141
    }
    return jsonify(result)
@api.route("/login")
def login():
    username = request.args["username"]
    print(username)
    result = {
        "computer": 131314,
        "brand": 1243141
    }
    return jsonify(result)





