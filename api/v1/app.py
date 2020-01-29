#!/usr/bin/python3
"""
App file
"""
from flask import Flask, Blueprint, jsonify, make_response
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(error):
    """
        Close session
    """
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """
        handle error 404
    """
    error = {"error": "Not found"}
    return make_response(jsonify(error), 404)

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    app.run(host='0.0.0.0',
            port=5000,
            threaded=True,
            debug=True)
