__author__ = "yzj"
__data__ = "2020/4/11 19:49"

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String


db = SQLAlchemy()
class User(db.Model):

    user_name = Column(String(50), nullable=False, unique=True)





