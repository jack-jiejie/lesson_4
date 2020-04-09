__author__ = "yin"
__data__ = "2020/4/9 13:14"


from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!aaabbb'

app.config.from_object('config')
app.run(host='0.0.0.0', debug=app.config["DEBUG"], port=5001)




