from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html", arg = "Test")

@auth.route('/logout')
def logout():
    return "logout route"

@auth.route('/register')
def register():
    return render_template("register.html")