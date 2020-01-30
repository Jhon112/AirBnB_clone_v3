#!/usr/bin/python3
"""
Views
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """Return ok status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stats():
    """
    return counter of each object
    """

    stats = {}
    stats['states'] = storage.count('State')
    stats['amenities'] = storage.count("Amenity")
    stats['users'] = storage.count("users")
    stats['cities'] = storage.count("City")
    stats['places'] = storage.count("Place")
    stats['reviews'] = storage.count("Review")

    return jsonify(stats)
