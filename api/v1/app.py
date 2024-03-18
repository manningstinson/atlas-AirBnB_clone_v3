#!/usr/bin/env python3
"""
Main module to run version 1 of the API.
"""
import os
from flask import Flask, jsonify
from werkzeug.exceptions import NotFound
from api.v1.views import app_views
from models import storage
from flask_cors import CORS  # Import CORS module

app = Flask(__name__)

app.register_blueprint(app_views)

# Configure CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.teardown_appcontext
def teardown_appcontext(exception):
    """Close storage."""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """Handler for 404 errors."""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
