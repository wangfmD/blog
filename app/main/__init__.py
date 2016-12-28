# _*_ coding: utf-8 _*_
"""
  main
  Desc:
  Maintainer: wangfm
  CreateDate: 2016/12/28
"""

from flask import Blueprint
main = Blueprint('main', __name__)

from . import views, errors