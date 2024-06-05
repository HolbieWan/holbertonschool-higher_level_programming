import json
import unittest
from flask import Flask
from flask.testing import FlaskClient


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_login_with_valid_credentials(self):
        # Prepare test data
        valid_credentials = {
            'username': 'john_doe',
            'password': 'password123'
        }
        users = {
            'john_doe': {
                'password': 'password123',
                'role': 'admin'
            }
        }

        # Mock the users dictionary
        self.app.users = users

        # Send a POST request to /login with valid credentials
        response = self.client.post(
            '/login',
            data=json.dumps(valid_credentials),
            content_type='application/json')

        # Check the response status code and content
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json)

    def test_login_with_invalid_credentials(self):
        # Prepare test data
        invalid_credentials = {
            'username': 'john_doe',
            'password': 'wrong_password'
        }
        users = {
            'john_doe': {
                'password': 'password123',
                'role': 'admin'
            }
        }

        # Mock the users dictionary
        self.app.users = users

        # Send a POST request to /login with invalid credentials
        response = self.client.post(
            '/login',
            data=json.dumps(invalid_credentials),
            content_type='application/json')

        # Check the response status code and content
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {"error": "Invalid credentials"})

    def test_login_with_missing_credentials(self):
        # Prepare test data
        missing_credentials = {}

        # Send a POST request to /login with missing credentials
        response = self.client.post(
            '/login',
            data=json.dumps(missing_credentials),
            content_type='application/json')

        # Check the response status code and content
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json, {
                "error": "Username and password required"})


if __name__ == '__main__':
    unittest.main()
