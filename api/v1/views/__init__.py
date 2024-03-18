#!/usr/bin/env python3
"""
Package initializer for views of version 1 of the API.
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Circular import is avoided by importing at the end
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *  # Add this line to import the cities view
