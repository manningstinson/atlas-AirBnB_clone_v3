from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Circular import is avoided by importing at the end
from api.v1.views.index import *
from . import users
