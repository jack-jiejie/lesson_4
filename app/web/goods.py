__author__ = "yzj"
__data__ = "2020/4/10 22:47"

from flask import jsonify, Blueprint

# 实例化蓝图对象
web = Blueprint('web', __name__)

@web.route("/getgoods")
def get_goods():
    result = {
        "computer": 9800,
        "brand": 1.8
    }
    return jsonify(result)





