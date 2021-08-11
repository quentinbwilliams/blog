"""Blog application."""

from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post

# INITIALIZE APP VARIABLE & CONFIGURE APP
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY']='fun'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


# CONNECT TO DB & MAKE TABLES
connect_db(app)
db.create_all()

# SERVE HOME ROUTE
@app.route('/', methods = ["GET"])
def home():
    """ Redirects to users route """
    
    # return render_template('index.html')
    return redirect('/users')

# SERVE USERS ROUTE
@app.route('/users', methods = ["GET"])
def get_all_users():
    """
    Access users in db
    """
    users = User.query.all()
    
    return render_template('users.html', users=users)

# SERVE USER INFO ROUTE
@app.route('/users/<int:user_id>', methods = ["GET"])
def show_user(user_id):
    """
    Show information about the given user.
    Have a button to get to their edit page, and to delete the user.
    """
    user = User.query.get_or_404(user_id)

    return render_template('user_profile.html', user=user)

# SERVE NEW USER ROUTE
@app.route('/users/new', methods = ["GET", "POST"])
def make_new_user():
    """ Create form to create a new user """
    username = request.form['username']
    first_name = request.form['first_name']
    last_name = request.form['last_name']


    new_user = User(username=username,
                    first_name=first_name,
                    last_name=last_name,
                    )
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(f"/users/{new_user.id}")

# HANDLE USER EDIT FORM ON USER INFO ROUTE
@app.route('/users/<int:user-id>/edit', methods = ["GET"])
def handle_edit_user_form():
    """
    Process the edit form, returning the user to the /users page.
    """

    return redirect('users.html')


    
# HANDLE USER DELETE FORM ON USER INFO ROUTE
@app.roue('/users/<int:user-id>/delete', methods = ["GET", "POST"])
def delete_user_form():
    """
    Delete the user.
    """
    
    
'''


# HANDLE NEW USER ROUTE
@app.route('/users/new', methods = ["GET", "POST"])
def handle_new_user_form():
    """
    Handle form to create a new user
    """
    
    return render_template('users.html')



# MAKE USER EDIT FORM ON USER INFO ROUTE
@app.route('/users/<int:user-id>/edit', methods = ["GET"])
def edit_user_form():
    """
    Show the edit page for a user.
    Have a cancel button that returns to the detail page for a user, and a save button that updates the user.
    """
    
    return render_template()



# SERVE USER NEW POST ROUTE
@app.route('/users/<int:user-id>/posts/new', methods = ["GET", "POST"])
def get_new_post():
    """
    Show form to add a post for that user.
    """
    
    return render_template()

# HANDLE NEW POST FORM ON USER NEW POST ROUTE
@app.route('/users/<int:user-id>/posts/new', methods = ["POST"])
def make_new_post():
    """
    Handle add form; add post and redirect to the user detail page. 
    """
    
    return render_template()

# SERVE POST ROUTE
@app.route('/posts/<int:post-id>', methods = ["GET"])
def show_posts():
    """
    Show a post & buttons to edit, delete post
    """
    
    return render_template()

# SERVE ROUTE TO EDIT POST
@app.route('/posts/<int:post-id>/edit', methods = ["GET"])
def create_edit_post_form():
    """
    Show form to edit post
    """
    
    return render_template()

# HANDLE EDIT POST FORM ON EDIT POST ROUTE
@app.route('/posts/<int:post-id>/edit', methods = ["POST"])
def handle_edit_post_form():
    """
    Handle form to edit post
    """
    
    return render_template()

# HANDLE DELETE POST ON EDIT POST ROUTE
@app.route('/posts/<int:post-id>/delete', methods = ["POST"])
def handle_delete_post_form():
    """
    Handle form to edit post
    """
    
    return render_template()





'''