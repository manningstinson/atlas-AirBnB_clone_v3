#!/usr/bin/python3
"""Module to configure and run the Flask application for the API."""

import os
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})

@app.teardown_appcontext
def teardown_appcontext(error):
    """Closes the database connection."""
    storage.close()

@app.errorhandler(404)
def handle_404_error(error):
    """Handles 404 Not Found errors."""
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    # Run the Flask application
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', '5000')))
