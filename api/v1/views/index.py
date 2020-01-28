#!/usr/bin/pyhton3
""" Views
"""
from api.v1.views import app_views
from flask import jsonify
from models import file_storage


@app_views.route('/status')
def status():
    """
        Return status `Ok`
    """
    return jsonify(status='OK')

def stats():
    """
        Return the number of each objects
    """
    stats = file_storage.count()
    return jsonify(**stats)

