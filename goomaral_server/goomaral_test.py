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

prefs = [
    'Hokkaido',
    'Aomori',
    'Iwate',
    'Miyagi',
    'Akita',
    'Yamagata',
    'Fukushima',
    'Ibaraki',
    'Tochigi',
    'Gunma',
    'Saitama',
    'Chiba',
    'Tokyo',
    'Kanagawa',
    'Niigata',
    'Toyama',
    'Ishikawa',
    'Fukui',
    'Yamanashi',
    'Nagano',
    'Gifu',
    'Shizuoka',
    'Aichi',
    'Mie',
    'Shiga',
    'Kyoto',
    'Osaka',
    'Hyogo',
    'Nara',
    'Wakayama',
    'Tottori',
    'Shimane',
    'Okayama',
    'Hiroshima',
    'Yamaguchi',
    'Tokushima',
    'Kagawa',
    'Ehime',
    'Kochi',
    'Fukuoka',
    'Saga',
    'Nagasaki',
    'Kumamoto',
    'Oita',
    'Miyazaki',
    'Kagoshima',
    'Okinawa']

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
        return redirect(url_for('top'))
    return render_template('index.html', user = user)

# route for top
@app.route("/top", methods=['GET', 'POST'])
def top():
    if g.user:
        print(g.user)
        user = g.user
    else:
        return redirect(url_for('login'))

    # setting pref id
    pref_id = 13    # defeault tokyo 13
    if request.form:
        pref_id = request.form['pref_id']
        print(request.form)

    # setting user language
    language = convert_country_to_language(user['country'])
    #sample_place = get_places_jp(language=language)
    sample_place = get_places_pref(pref_id=pref_id, language = language, size = 10)

    data = {'pref_id': prefs[int(pref_id)-1]}
    return render_template('top.html', data = data, places = sample_place, user = user, language = language)

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
        return redirect(url_for('top'))
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
            return redirect(url_for('top'))
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registers the user."""

    print(request)
    if g.user:
        return redirect(url_for('top'))
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
    places = get_places_jp(language='ko', size=5)
    for place in places:
        print place['id'], place['score']
    return "ok"

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
