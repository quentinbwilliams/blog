"""Models for Blog."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    
    db.init_app(app)


class User(db.Model):
    """
    username: required,
    first_name: required,
    last_name: required,
    image_url: optional,
    """
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    username = db.Column(db.String(25), unique=True, nullable=False)
    
    first_name = db.Column(db.String(30), unique=False, nullable=False)

    last_name = db.Column(db.String(30), unique=False, nullable=False)
    
    image_url = db.Column(db.String(), unique=False, nullable=True)
    
    # posts = db.relationship('Post')
    
    def __repr__(self):
        return f"<User {self.username} {self.first_name} {self.last_name}>"

    
class Post(db.Model):
    """
    title: required,
    content: optional,
    author_id: required
    """
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    title = db.Column(db.Text, nullable=False, unique=True)
    
    content = db.Column(db.Text, nullable=True)
    
    date_created = db.Column(db.Text, nullable=False)
    
    # author = db.relationship('User')
    
    def __repr__(self):
        return f"<Post {self.title} {self.content} {self.date_created}>"
