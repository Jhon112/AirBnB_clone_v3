#!/usr/bin/pyhton3
""" Views
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """
        Return status `Ok`
    """
    return jsonify(status='OK')


@app_views.route('/stats', strict_slashes=False)
def stats():
    """
        Return the number of each objects
    """
    stats = {"amenities": storage.count('Amenity'),
             "cities": storage.count('City'),
             "places": storage.count('Place'),
             "reviews": storage.count('Review'),
             "states": storage.count('State'),
             "users": storage.count('User')}
    return jsonify(stats)
