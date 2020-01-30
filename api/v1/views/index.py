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
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """
        Return the number of each objects
    """
    stats = {}
    stats['states'] = storage.count("State")
    stats['cities'] = storage.count("City")
    stats['amenities'] = storage.count("Amenity")
    stats['places'] = storage.count("Place")
    stats['users'] = storage.count("User")
    stats['reviews'] = storage.count("Review")
    return jsonify(stats)
