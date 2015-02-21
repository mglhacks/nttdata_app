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
from flask import g


### Variables
DATABASE = './database.db'

### Create app
# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)

### DATABASE
def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        top.sqlite_db = sqlite3.connect(app.config['DATABASE'])
        top.sqlite_db.row_factory = sqlite3.Row
    return top.sqlite_db

@app.teardown_appcontext
def close_database(exception):
    """Closes the database again at the end of the request."""
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()


def init_db():
    """Creates the database tables."""
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
    # add post1
    # add_post(1)

def query_db(query, args=(), one=False):
    """Queries the database and returns a list of dictionaries."""
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    return (rv[0] if rv else None) if one else rv
########

# route for INDEX
@app.route("/")
def hello():
    return render_template('index.html')

# route for PROFILE
@app.route("/profile", methods=['GET', 'POST'])
def profile():
	pref_id = 13
	print("profile", request)
	sample_place = query_db('''select * from places where id = 1''', one=True)
	if request.form:
		pref_id = request.form['pref_id']
		print(request.form)
	ranking1 = [  {'name':"Hachiko", 'comment':"comment1"}, 
				{'name':"Meijijingu", 'comment':"comment2"},
				{'name':sample_place['name']
				, 'comment':sample_place['website']} ]
	data = {'pref_id':pref_id, 'category1': "category1", 'category2':"category2", 'ranking1':ranking1}
	return render_template('profile.html', data = data)

# tests
@app.route('/hello/')
@app.route('/hello/<name>')
def hello_template(name=None):
	return render_template('hello.html', name=name)

@app.route('/test')
def test_page():
	return render_template('test.html')

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
