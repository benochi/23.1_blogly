"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

DEFAULT_IMG = "https://unsplash.com/photos/4kCGEB7Kt4k"

class User(db.Model):
    """user model for site"""
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMG)

    @property
    def full_name(self):
        """User full_name"""
        return f"{self.first_name} {self.last_name}"

def connect_db(app):
    """connects this databse to the provided Flask app"""

    db.app = app
    db.init_app(app)
