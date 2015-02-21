# -*- coding: utf-8 -*-

import requests # Requests is recommended over urllib*
import json
import sqlite3
import os.path

API_KEY = 'AIzaSyBBN84m4bDAzLnE1dhZ-QpDtAJcq-upOes'
DB = 'from_google.db'

def search_api(query, types=''):
    """Places Text Search API: returns json results,
    documentation: https://developers.google.com/places/documentation/search"""
    base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    params = {'key' : API_KEY, 'query' : query}
    if types != '':
        params['types'] = types
    response = requests.get(base_url, params=params)
    return response.json()

def details_api(placeid, language=''):
    """Places Details API: returns json results,
    documentation: https://developers.google.com/places/documentation/details"""
    base_url = 'https://maps.googleapis.com/maps/api/place/details/json'
    params = {'key' : API_KEY, 'placeid' : placeid}
    if language != '':
        params['language'] = language
    response = requests.get(base_url, params=params)
    return response.json()

def gplus_api(userid):
    """Google Plus API: returns json results,
    documentation: https://developers.google.com/+/api/latest/people/get"""
    base_url = 'https://www.googleapis.com/plus/v1/people/' + userid
    params = {'key' : API_KEY}
    response = requests.get(base_url, params=params)
    return response.json()

def store_place(res, conn):
    values = []
    values.append(res.get('website'))
    values.append(res.get('rating'))
    values.append(res.get('utc_offset'))
    values.append(res.get('user_ratings_total'))
    values.append(res.get('name'))
    values.append(res.get('photos'))
    values.append(res.get('geometry'))
    values.append(res.get('adr_address'))
    values.append(res.get('place_id'))
    values.append(res.get('international_phone_number'))
    values.append(res.get('vicinity'))
    values.append(res.get('reviews'))
    values.append(res.get('url'))
    values.append(res.get('address_components'))
    values.append(res.get('formatted_address'))
    values.append(res.get('types'))
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
    values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, tuple(values))
    conn.commit()

def main_work(place_names):
    conn = sqlite3.connect(DB)
    for pn in place_names:
        # search place
        search_results = search_api(pn)
        # get details without specifying language
        details = details_api()
        store_place(search_results['results'][0], conn)
        # save raw search results into the database
        # save search results into the database
        # get details of the top place for each language

def db_init():
    """Initializes a database with necessarry empty tables"""
    conn = sqlite3.connect(DB)
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

# Examples:
# overview = search_api("tokyo university")
# print json.dumps(overview, indent=2, ensure_ascii=False).encode('utf8')
# details = details_api(overview['results'][0]['place_id'], 'cn')
# print json.dumps(details, indent=2, ensure_ascii=False).encode('utf8')
# print json.dumps(gplus_api('107668880099887403676'), indent=2, ensure_ascii=False).encode('utf8')
db_init();
main_work({'university tokyo'})
