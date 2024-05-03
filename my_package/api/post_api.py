# my_package/api/post_api.py
from flask import Blueprint, jsonify
from my_package.models.post import Post  # Importing the Post class from the models module

post_api = Blueprint('post_api', __name__)

# Sample data for demonstration
posts = [
    Post(title='Post 1', content='Content of Post 1', author='Author 1'),
    Post(title='Post 2', content='Content of Post 2', author='Author 2')
]

@post_api.route('/posts', methods=['GET'])
def get_posts():
    return jsonify([post.__dict__ for post in posts])
