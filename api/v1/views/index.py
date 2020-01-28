#!/usr/bin/pyhton3
""" Views
"""
from api.v1.views import app_views
from flask import jsonify
from models.engine import file_storage


@app_views.route('/status')
def status():
    """
        Return status `Ok`
    """
    return jsonify(status='OK')

@app_views.route('/stats')
def stats(self):
    """
        Return the number of each objects
    """
    stats = self.count()
    return jsonify(**stats)

