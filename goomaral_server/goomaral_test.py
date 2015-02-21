"""
2015/02/21
NTT Data Hackathon
Goo Maral Application
"""

# flask imports
from flask import Flask, request, session, url_for, redirect, render_template, abort, g, flash, _app_ctx_stack, jsonify, send_from_directory
from werkzeug import check_password_hash, generate_password_hash
from flask.ext.restful import reqparse, abort, Api, Resource
from werkzeug import secure_filename
import json
from flask_bootstrap import Bootstrap

import sqlite3

# user imports
from database_helper import *

### Variables
DATABASE = './database.db'
PER_PAGE = 30
DEBUG = True
SECRET_KEY = 'burtechono'

### Create app
# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)

# route for INDEX
@app.route("/")
def hello():
    user = None
    if g.user:
        print(g.user)
        user = g.user
    return render_template('index.html', user = user)

# route for PROFILE
@app.route("/profile", methods=['GET', 'POST'])
def profile():
    if g.user:
        print(g.user)
        user = g.user
    else:
        return redirect(url_for('login'))

    pref_id = 13
    print("profile", request)
    sample_place = get_place(1)
    if request.form:
        pref_id = request.form['pref_id']
        print(request.form)
    ranking1 = [  {'name':"Hachiko", 'comment':"comment1"},
                {'name':"Meijijingu", 'comment':"comment2"},
                {'name':sample_place['name']
                , 'comment':sample_place['website']} ]
    data = {'pref_id':pref_id, 'category1': "category1", 'category2':"category2", 'ranking1':ranking1}
    return render_template('profile.html', data = data, user = user)

### LOGIN process
@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = query_db('select * from user where user_id = ?',
                          [session['user_id']], one=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Logs the user in."""
    if g.user:
        return redirect(url_for('profile'))
    error = None
    if request.method == 'POST':
        user = query_db('''select * from user where
            email = ?''', [request.form['email']], one=True)
        if user is None:
            error = 'Invalid username'
        elif not check_password_hash(user['pw_hash'],
                                     request.form['password']):
            error = 'Invalid password'
        else:
            flash('You were logged in')
            session['user_id'] = user['user_id']
            return redirect(url_for('profile'))
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registers the user."""

    print(request)
    if g.user:
        return redirect(url_for('profile'))
    error = None
    if request.method == 'POST':
        if not request.form['username']:
            error = 'You have to enter a username'
        elif not request.form['email'] or \
                 '@' not in request.form['email']:
            error = 'You have to enter a valid email address'
        elif not request.form['password']:
            error = 'You have to enter a password'
        elif request.form['password'] != request.form['password2']:
            error = 'The two passwords do not match'
        elif get_user_id(request.form['email']) is not None:
            error = 'The email is already registered'
        elif not request.form['country']:
            error = 'You have to specify your country'
        else:
            db = get_db()
            db.execute('''insert into user (
              username, email, pw_hash, country) values (?, ?, ?, ?)''',
              [request.form['username'], request.form['email'],
               generate_password_hash(request.form['password']), request.form['country']])
            db.commit()
            flash('You were successfully registered and can login now')
            return redirect(url_for('login'))
    return render_template('index.html', error=error)


@app.route('/logout')
def logout():
    """Logs the user out."""
    flash('You were logged out')
    session.pop('user_id', None)
    return redirect(url_for('hello'))

# tests
@app.route('/hello/')
@app.route('/hello/<name>')
def hello_template(name=None):
    return render_template('hello.html', name=name)

@app.route('/test')
def test_page():
    return render_template('test.html')

@app.route("/test_db", methods=['GET'])
def test_db():
    return str(get_places_jp('es'))

### static file helpers
# route for static js, css files
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)
@app.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory('static/fonts', path)
@app.route('/font-awesome/<path:path>')
def send_fontawesome(path):
    return send_from_directory('static/font-awesome', path)
@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('static/img', path)
@app.route('/less/<path:path>')
def send_less(path):
    return send_from_directory('static/less', path)

# main
if __name__ == "__main__":

    app.debug = True
    app.run(host="0.0.0.0")
