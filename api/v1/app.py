#!/usr/bin/python3
"""app.py: Module to configure and run the Flask application for the API"""

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
    """Teardown app context: Closes the database connection"""
    storage.close()

@app.errorhandler(404)
def page_not_found(error):
    """Error handler for 404 Not Found"""
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', '5000')))
