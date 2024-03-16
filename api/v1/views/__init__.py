#!/usr/bin/python3
"""Initializes the views package for the v1 API."""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# Avoid circular import errors
from api.v1.views.index import *
