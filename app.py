"""Blog application."""

from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY']='fun'

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home():
    """ """
    
    return render_template('index.html')

@app.route('/users')
def show_all_users():
    """ """
    
    return render_template('users.html')

@app.route('/users', methods = ["POST"])
def make_new_user():
    """ """
    
    return render_template('users.html')