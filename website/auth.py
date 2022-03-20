from flask import Blueprint, render_template, request
import requests

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        payload = {'username': username, 'password': password}
        url = "https://family-task-api.herokuapp.com/auth"

        response = requests.post(url, json = payload)
        access_token = response.json()['access_token']

    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "logout route"

@auth.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        payload = {'username': username, 'password': password}
        url = "https://family-task-api.herokuapp.com/register"

        response = requests.post(url, json = payload)

        if len(username) < 4:
            pass
        elif len(password) < 6:
            pass
        else:
            #add user to db
            pass

    return render_template("register.html")