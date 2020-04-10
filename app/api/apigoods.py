__author__ = "yzj"
__data__ = "2020/4/10 22:47"

from flask import jsonify, Blueprint

# 实例化蓝图对象
# api = Blueprint('api', __name__)
from . import api

@api.route("/goods")
def goods():
    result = {
        "computer": 11119800,
        "brand": 11111.8
    }
    return jsonify(result)





