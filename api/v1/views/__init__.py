#!/usr/bin/python3
"""Initialize Blueprint views for API v1"""

from flask import Blueprint

# Create a Blueprint instance for API v1 views
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# Import specific views from respective modules
from . import index
from . import amenities
from . import cities
from . import places
from . import places_amenities
from . import places_reviews
from . import states
from . import users
