#!/usr/bin/pyhton3
"""
"""
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status')
def status():
    """
        Return status `Ok`
    """
    return jsonify(status='OK')

