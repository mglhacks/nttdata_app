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

import sqlite3
from operator import itemgetter

# user imports
from goomaral_test import app, DATABASE

### DATABASE basic functions
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        top.sqlite_db = sqlite3.connect(app.config['DATABASE'])
        # top.sqlite_db.row_factory = sqlite3.Row
        top.sqlite_db.row_factory = dict_factory
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

### Getter and setters
def get_place(id):
    """Returns one place by id"""
    place = query_db('''select * from places where places.id = ?''', [id], one=True)
    return place

def get_places_jp(language='en', size=5):
    """Returns top places of all Japan"""
    places = query_db('''select * from places''')
    add_scores(places, language)
    places_sorted = sorted(places, key=itemgetter('score'))
    return places_sorted[0:size]

def get_places_pref(pref_id, language='en', size=5):
    """Returns top places of all Japan"""
    places = query_db('''select * from places where pref_id = ?''', (pref_id))
    add_scores(places, language)
    places_sorted = sorted(places, key=itemgetter('score'))
    return places_sorted[0:size]

def get_post2(post_id):
    """Returns one post by post_id"""
    post = query_db('''select * from post where post.post_id = ?''', [post_id], one=True)
    return post

def get_post3(post_id):
    """Returns one post by post_id"""
    post = query_db('''select * from post where post.post_id = ?''', [post_id], one=True)
    return post

# login db
def get_user_id(email):
    """Convenience method to look up the id for a username."""
    rv = query_db('select user_id from user where email = ?',
                  [email], one=True)
    return rv[0] if rv else None

### Inner methods
def add_scores(places, language):
    """Adds calculated score to each place (modifies the passed places list)"""
    # TODO: calculation
    for p in places:
        reviews = query_db('''select * from reviews where place_id = ? and language = ?''',\
                           (p['place_id'], language))
        if len(reviews) == 0:
            # No review found for this language
            p['score'] = p['rating']
        else:
            ratings = [r['rating'] for r in reviews]
            p['score'] = sum(ratings) / float(len(reviews))
