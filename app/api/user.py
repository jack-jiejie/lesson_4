__author__ = "yzj"
__data__ = "2020/4/10 22:47"

from flask import jsonify, Blueprint, request

# 实例化蓝图对象
# user = Blueprint('web', __name__)
from . import api
from ..forms.user import UserForm


@api.route("/users")
def users():
    result = {
        "computer": 131314,
        "brand": 1243141
    }
    return jsonify(result)
@api.route("/login")
def login():
    # 接收消息
    # username = request.args["username"]
    # print(username)
    form = UserForm(request.args)

    if form.validate():
        username = form.username.data.strip()
        print(username)
        result = {
            "status": 2001,
            "message": "叫"
        }
        return jsonify(result)
    else:
        return jsonify(form.errors)
    # return jsonify(result)

@api.route("/getuserinfo", methods = ["GET", "POST"])
def get_user_info():
    if request.method == "GET":
        form = UserForm(request.args)
        print("get请求来了")
    if request.method == "POST":
        print("post请求来了")
    return "这把有效了"

