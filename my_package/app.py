# my_package/app.py
from flask import Flask
from my_package.api.post_api import post_api  # Importing the post_api Blueprint

app = Flask(__name__)

# Registering the post_api Blueprint
app.register_blueprint(post_api)

if __name__ == '__main__':
    app.run(debug=True)
