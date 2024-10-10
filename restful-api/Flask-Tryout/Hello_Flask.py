from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

class User:
    def __init__(self, username, theme, image):
        self.username = username
        self.theme = theme
        self.image = image

    def to_json(self):
        # Convert the user object to a dictionary
        return {
            "username": self.username,
            "theme": self.theme,
            "image": self.username + "image"
        }

# Mock function to return the current user
def get_current_user():
    return User(username="john_doe", theme="dark", image="john_profile.png")

# Mock function to return a list of users
def get_all_users():
    return [
        User(username="john_doe", theme="dark", image="john_profile.png"),
        User(username="jane_smith", theme="light", image="jane_profile.png"),
        User(username="admin", theme="dark", image="admin_profile.png"),
    ]

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": user.image
    }

@app.route("/users")
def users_api():
    users = get_all_users()
    return [user.to_json() for user in users]

if __name__ == "__main__":
    app.run(debug=True)