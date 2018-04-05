#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
app = Flask(__name__)
#配置数据库地址
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:sa@localhost/car_db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#该配置为True,则每次请求结束都会自动commit数据库的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True
db = SQLAlchemy(app)
#也可以db = SQLAlchemy()        db.init_app(app)