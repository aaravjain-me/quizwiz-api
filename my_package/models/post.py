# my_package/models/post.py
from datetime import datetime

class Post:
    def __init__(self, title, content, author, created=None):
        self.title = title
        self.content = content
        self.author = author
        self.created = created or datetime.utcnow()

    def __repr__(self):
        return f'<Post {self.title}>'
