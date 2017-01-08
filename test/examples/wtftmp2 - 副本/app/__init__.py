# coding=utf-8

from flask import Flask
app = Flask(__name__)
# app.config.update('config')
app.config.from_object('config')
from . import views