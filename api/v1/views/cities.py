#!/usr/bin/python3
"""
    View Cities
"""

from api.v1.views import app_views
from flask import Flask, jsonify, abort, make_response, request
from models.city import City
from models import storage
import json


@app_views.route('/states/<state_id>/cities', strict_slashes=False)
def cities(state_id):
    """
    Return all cities of a state
    """
    all_cities = storage.all('City').values()
    cities_object = [obj.to_dict() for obj in all_cities]

    state = [city for city in cities.to_dict() if conditional city if city.state_id == state_id for city in]


# @app_views.route('/cities/<state_id>', strict_slashes=False)
# def list_cities(state_id):
#     """
#         Retrieves a State object
#     """
#     state = storage.get('City', state_id)
#     if state is None:
#         abort(404)
#     state = state.to_dict()

#     return jsonify(state)


# @app_views.route('/cities/<state_id>', methods=['DELETE'],
#                  strict_slashes=False)
# def delete_state(state_id):
#     """
#         deletes a State object
#     """
#     state = storage.get('City', state_id)
#     if state is None:
#         abort(404)

#     storage.delete(state)
#     storage.save()

#     return make_response(jsonify({}), 200)


# @app_views.route('/cities', methods=['POST'], strict_slashes=False)
# def post_state():
#     """
#         post a State object
#     """
#     if not request.json:
#         abort(400, "Not a JSON")
#     data = request.json
#     if 'name' not in data.keys():
#         abort(400, "Missing name")
#     instance = City(**data)
#     storage.new(instance)
#     storage.save()

#     return make_response(jsonify(instance.to_dict()), 201)


# @app_views.route('/cities/<state_id>', methods=['PUT'], strict_slashes=False)
# def update_state(state_id):
#     """
#         update a State object
#     """
#     state = storage.get('City', state_id)
#     if state is None:
#         abort(404)

#     if not request.json:
#         abort(400, "Not a JSON")

#     data = request.json
#     for key, value in data.items():
#         setattr(state, key, value)

#     storage.save()

#     return make_response(jsonify(state.to_dict()), 200)
