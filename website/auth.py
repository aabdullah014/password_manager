from tabnanny import check
from flask import Blueprint, render_template, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib
import requests


auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password').encode()
        hash_password = hashlib.sha256(password).hexdigest()
        payload = {'username': username, 'password': hash_password}
        print(password)
        print(payload)
        url = "https://family-task-api.herokuapp.com/auth"

        response = requests.post(url, json = payload)
        print(response.json())
        # access_token = response.json()['access_token']
        # print(access_token)

    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "logout route"

@auth.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password').encode()

        #only 20 characters because server won't take more than 20.
        hash_password = hashlib.sha256(password).hexdigest()

        payload = {'username': username, 'password': hash_password}
        url = "https://family-task-api.herokuapp.com/register"


        if len(username) < 4:
            flash('Username must be at least 4 characters!', category = "error")
        elif len(password) < 6:
            flash('Password must be at least 6 characters!', category = "error")
        else:
            #add user to db
            response = requests.post(url, params = payload)
            print(password)
            print(payload)
            print(response.json())
            flash('Successfully registered!', category = "success")

    return render_template("register.html")