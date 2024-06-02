#!/usr/bin/python3
"""Creating a simple server Module"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """Default endpoint for homepage"""
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    """Endpoint returning a JSON response with all users dictionary keys (usernames)"""
    names = list(users.keys())
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
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route('/add_user', methods=['POST'])
def add_user():
    """Endpoint to add a new user"""
    new_user = request.get_json
    username = new_user['username']
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = new_user
    return jsonify({'message': 'User added', 'user': new_user}), 201


if __name__ == "__main__":
    app.run()
