__author__ = "yzj"
__data__ = "2020/4/10 23:05"
from flask import Blueprint
api = Blueprint('api', __name__)

from app.api import apigoods
from app.api import user








