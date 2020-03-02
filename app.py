# app.py
from flask import Flask
import mysql.connector
import config

app = Flask(__name__)
app.config['SECRET_KEY'] = config.app['secret_key']

# 在app之后引入, 否则会循环依赖, 因为user中引入了本文件的app
from controller.user.user import *


if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1', port=9990)
