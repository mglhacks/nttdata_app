# -*- coding: utf-8 -*-

import sqlite3
import os.path
import json

DB = 'honban-new.db'
conn = sqlite3.connect(DB)

def query_db(query, args=(), one=False):
    """Queries the database and returns a list of dictionaries."""
    cur = conn.execute(query, args)
    rv = cur.fetchall()
    return (rv[0] if rv else None) if one else rv

def get_place(place_id):
    """Returns one place by id"""
    place = query_db('''select * from places where place_id = ?''', [place_id], one=True)
    return place

def save_raw_results(response, table):
    conn.execute("""insert into %s(url, result) values (?, ?)"""%(table),\
                 (response.url, json.dumps(response.json())))
    conn.commit()

def save_review(place_id, review):
    """Save review into the database"""
    values = [place_id]
    values.append(review.get('rating'))
    values.append(review.get('aspects')[0].get('rating'))
    values.append(review.get('aspects')[0].get('type'))
    values.append(review.get('language'))
    values.append(review.get('text'))
    values.append(review.get('author_name'))
    values.append(review.get('author_url'))
    values.append(review.get('time'))
    conn.execute("""insert into reviews(place_id, rating, aspects_rating,
    aspects_type, language, text, author_name, author_url, time) values (?, ?, ?, ?, ?, ?, ?, ?, ?)""",\
                 tuple(values))
    conn.commit()

def save_name(place_id, name, language):
    conn.execute("""insert into names(place_id, name, language) values (?, ?, ?)""", (place_id, name, language))
    conn.commit()

def save_place_details(details, pref_id=0, rurubu_pref_rank=0):
    """Save place details into the database"""
    values = []
    values.append(details.get('website'))
    values.append(details.get('rating'))
    values.append(details.get('utc_offset'))
    values.append(details.get('user_ratings_total'))
    values.append(details.get('name'))
    values.append(json.dumps(details.get('photos')))
    values.append(json.dumps(details.get('geometry')))
    values.append(details.get('adr_address'))
    values.append(details.get('place_id'))
    values.append(details.get('international_phone_number'))
    values.append(details.get('vicinity'))
    values.append(json.dumps(details.get('reviews')))
    values.append(details.get('url'))
    values.append(json.dumps(details.get('address_components')))
    values.append(details.get('formatted_address'))
    values.append(json.dumps(details.get('types')))
    values.append(details.get('icon'))
    values.append(pref_id)
    values.append(rurubu_pref_rank)
    conn.execute("""insert into places(
    website,
    rating,
    utc_offset,
    user_ratings_total,
    name,
    photos,
    geometry,
    adr_address,
    place_id,
    international_phone_number,
    vicinity,
    reviews,
    url,
    address_components,
    formatted_address,
    types,
    icon,
    pref_id,
    rurubu_pref_rank)
    values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, tuple(values))
    conn.commit()

def db_init():
    """Initializes a database with necessarry empty tables"""
    conn.execute('''create table if not exists places
    (id integer primary key not null,
    website text,
    rating real,
    utc_offset integer,
    user_ratings_total integer,
    name text not null,
    photos text,
    geometry text not null,
    adr_address text,
    place_id text not null,
    international_phone_number text,
    vicinity text,
    reviews text,
    url text,
    address_components text,
    formatted_address text,
    types text,
    icon text,
    pref_id integer,
    rurubu_pref_rank integer);''')

    conn.execute('''create table if not exists names
    (id integer primary key not null,
    place_id text not null,
    name text not null,
    language text not null);''')

    conn.execute('''create table if not exists reviews
    (id integer primary key not null,
    place_id text not null,
    rating integer not null,
    aspects_rating integer not null,
    aspects_type text,
    language text not null,
    text text,
    author_name text,
    author_url text,
    time integer not null);''')

    conn.execute('''create table if not exists search_raw
    (id integer primary key not null,
    url text not null,
    result text not null);''')

    conn.execute('''create table if not exists details_raw
    (id integer primary key not null,
    url text not null,
    result text not null);''')

    conn.execute('''create table if not exists gplus_raw
    (id integer primary key not null,
    url text not null,
    result text not null);''')

    conn.commit()
