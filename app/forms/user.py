__author__ = "yzj"
__data__ = "2020/4/11 15:07"

from wtforms import Form, StringField
from wtforms.validators import DataRequired, length


class UserForm(Form):
    username = StringField(validators=[DataRequired(), length(min=5, max=10)])






