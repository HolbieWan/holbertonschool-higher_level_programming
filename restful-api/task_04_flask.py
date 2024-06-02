#!/usr/bin/python3
"""Creating a simple server Module"""

from flask import Flask, jsonify, request
from markupsafe import escape

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
    """Endpoint returning a JSON response with dictionary keys (usernames)"""
    names = list(users.keys())
    return jsonify(names)


@app.route('/status')
def status():
    """Default endpoint returning the status of the API"""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Endpoint returning a JSON response with the user details"""
    username = escape(username)
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route('/add_user', methods=['POST'])
def add_user():
    """Endpoint to add a new user"""
    new_user = request.get_json()
    if not new_user:
        return jsonify({"error": "Invalid JSON data"}), 400
    username = new_user.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    username = escape(username)
    new_user['username'] = username
    users[username] = new_user
    return jsonify({'message': 'User added', 'user': new_user}), 201


if __name__ == "__main__":
    app.run(port=8000)

