from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "login route"

@auth.route('/logout')
def logout():
    return "logout route"

@auth.route('/register')
def register():
    return "register route"