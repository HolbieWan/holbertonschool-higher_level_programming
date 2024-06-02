#!/usr/bin/python3
"""Creating a simple server Module"""

from flask import Flask, jsonify, abort

app = Flask(__name__)

users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"},
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"}}


@app.route('/')
def home():
    """Default endpoint for homepage"""
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    """Endpoint returning a JSON response with all usernames"""
    names = [user["name"] for user in users.values()]
    return jsonify(names)

@app.route('/status')
def status():
    """Default endpoint returning the status of the API"""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Endpoint returning a JSON response with the user details"""
    user = users.get(username)
    if user is None:
        abort(404, description="User not found")
    return jsonify(user)

if __name__ == "__main__":
    app.run()
