__author__ = "yzj"
__data__ = "2020/4/10 22:43"

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    # 蓝图注册
    register_blueprint(app)
    return app

def register_blueprint(app):
    from app.web.goods import web
    from app.api import api
    # from app.api.apigoods import api
    app.register_blueprint(api)
    app.register_blueprint(web)
    # app.register_blueprint(user)







