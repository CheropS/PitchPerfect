'''
paths
route for login, logout and register
queries-to check for available pitches
'''
from flask import render_template
from . import auth

@auth.route('/login')
def login():
    return render_template('auth/login.html')