"""Models for Blog."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    
    db.init_app(app)


class User(db.Model):
    """ """
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first_name = db.Column(db.String(80), unique=False, nullable=False)

    last_name = db.Column(db.String(80), unique=False, nullable=False)
    
    image_url = db.Column(db.String(), unique=False, nullable=True)