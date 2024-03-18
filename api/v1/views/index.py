#!/usr/bin/env python3
"""
Module defining routes for version 1 of the API.
"""
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'])
def get_status():
    """Get status of the API."""
    return jsonify({"status": "OK"})
