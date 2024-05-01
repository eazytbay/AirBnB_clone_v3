#!/usr/bin/python3
"""
This Flask route returns json status response
"""
from api.v1.views import app_views
from flask import jsonify, request
from models import storage
from flasgger import swag_from


@app_views.route('/status', methods=['GET'])
@swag_from('swagger_spec/status.yml')
def status():
    """
    function for status route that returns the status
    """
    if request.method == 'GET':
        resp = {"status": "OK"}
        return jsonify(resp)


@app_views.route('/stats', methods=['GET'])
@swag_from('swagger_spec/stats.yml')
def stats():
    """
    function to return the count of all class objects
    """
    if request.method == 'GET':
        response = {}
        PLURALS = {
            "Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"
        }
        for key, value in PLURALS.items():
            response[value] = storage.count(key)
        return jsonify(response)
