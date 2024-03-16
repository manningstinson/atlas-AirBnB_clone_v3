#!/usr/bin/python3
"""Routes for handling status and statistics requests for the API."""

from flask import jsonify
from models import storage
from . import app_views

# Configuration for statistics
HBNB_TEXT = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def hbnb_status():
    """Returns the status of the API."""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def hbnb_stats():
    """Returns statistics about the number of objects in the storage."""
    return_dict = {}
    for key, value in HBNB_TEXT.items():
        return_dict[key] = storage.count(value)
    return jsonify(return_dict)
