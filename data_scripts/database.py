# -*- coding: utf-8 -*-

import sqlite3
import os.path
import json

def store_place(res, conn):
    values = []
    values.append(res.get('website'))
    values.append(res.get('rating'))
    values.append(res.get('utc_offset'))
    values.append(res.get('user_ratings_total'))
    values.append(res.get('name'))
    values.append(json.dumps(res.get('photos')))
    values.append(json.dumps(res.get('geometry')))
    values.append(res.get('adr_address'))
    values.append(res.get('place_id'))
    values.append(res.get('international_phone_number'))
    values.append(res.get('vicinity'))
    values.append(json.dumps(res.get('reviews')))
    values.append(res.get('url'))
    values.append(json.dumps(res.get('address_components')))
    values.append(res.get('formatted_address'))
    values.append(json.dumps(res.get('types')))
    values.append(res.get('icon'))
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
    icon)
    values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, tuple(values))
    conn.commit()

def db_init(db):
    """Initializes a database with necessarry empty tables"""
    conn = sqlite3.connect(db)
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
    icon text);''')
    conn.commit()
