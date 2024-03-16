#!/usr/bin/python3
"""Defines the routes for the v1 API status."""
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def api_status():
    """Returns the status of the API."""
    return jsonify({"status": "OK"})
