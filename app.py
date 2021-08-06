"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'shhh'

toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home():
    """homepage redirect list of Users"""
    return redirect("/users")

@app.route("/users")
def users():
    """Page of all current users"""
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template("/users/index.html", users=users)

@app.route("/users/new")
def new_user_form():
    """shows form for new user input"""
    return render_template("users/new-user.html")

@app.route("/users/new", methods=["POST"])
def new_users():
    """handles form submission of new_user_form"""

    new_user = User(
        first_name = request.form['first_name'],
        last_name = request.form['last_name'],
        image_url = request.form['image_url'] or None
    )

    db.session.add(new_user)
    db.session.commit()

    return redirect("/users")

@app.route("/users/<int:user_id>")
def show_users():
    """shows a page with info on a user using their user_id"""

    user = User.query.get_or_404(user_id)
    return render_template('users/show.html', user=user)

@app.route("/users/<int:user_id>/edit")
def edit_users():
    """Shows the edit page for a user and a cancel button that returns to the detail page for a user, 
    and a save button that updates the user.""" 

    user = User.query.get_or_404(user_id)
    return render_template('users/edit.html', user=user)

@app.route("/users/<int:user_id>/edit", methods=["POST"])
def update_users():
    """Handle the form submission for edit_users"""

    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name'],
    user.last_name = request.form['last_name'],
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect("/users")



