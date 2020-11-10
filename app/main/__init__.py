# -*- coding: utf-8 -*-

from flask import Blueprint

prefix_module = '/'

bp = Blueprint(prefix_module, __name__)

from app.main import routes
