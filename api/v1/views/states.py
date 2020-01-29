#!/usr/bin/python3
"""
    View State
"""

from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
# from requests import get


@app_views.route('/states')
def states():
    """
    """
    all_states = storage.all('States').values()
    states = list()
    for obj in all_states:
        states.append(obj.to_dict())

    return jsonify(states)


@app_views.route('/states/<state_id>')
def list_states(state_id):
    """
        Retrieves a State object
    """
    state = storage.get('State', state_id)
    if state is None:
        abort(404)
    state = state.to_dict()

    return jsonify(state)


