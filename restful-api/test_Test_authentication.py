import unittest
import json
from flask import Flask
from flask.testing import FlaskClient
from werkzeug.security import generate_password_hash

from Test_authentication import app

class AuthenticationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index_with_valid_credentials(self):
        # Prepare test data
        valid_credentials = ('john', 'hello')

        # Send a GET request to /
        response = self.app.get('/', headers=self.get_auth_header(*valid_credentials))

        # Check the response status code and content
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello, john!")

    def test_index_with_invalid_credentials(self):
        # Prepare test data
        invalid_credentials = ('john', 'wrong_password')

        # Send a GET request to /
        response = self.app.get('/', headers=self.get_auth_header(*invalid_credentials))

        # Check the response status code and content
        self.assertEqual(response.status_code, 401)

    def get_auth_header(self, username, password):
        # Generate Basic Auth header
        auth_header = {
            'Authorization': 'Basic ' + generate_password_hash(f'{username}:{password}')
        }
        return auth_header

if __name__ == '__main__':
    unittest.main()