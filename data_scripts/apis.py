# -*- coding: utf-8 -*-

import requests # Requests is recommended over urllib*
import json

from database import *

API_KEY = 'AIzaSyBBN84m4bDAzLnE1dhZ-QpDtAJcq-upOes'

def search_api(query, types=''):
    """Places Text Search API: returns json results,
    documentation: https://developers.google.com/places/documentation/search"""
    base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    params = {'key' : API_KEY, 'query' : query}
    if types != '':
        params['types'] = types
    response = requests.get(base_url, params=params)
    save_raw_results(response, 'search_raw')
    return response.json()

def details_api(placeid, language=''):
    """Places Details API: returns json results,
    documentation: https://developers.google.com/places/documentation/details"""
    base_url = 'https://maps.googleapis.com/maps/api/place/details/json'
    params = {'key' : API_KEY, 'placeid' : placeid}
    if language != '':
        params['language'] = language
    response = requests.get(base_url, params=params)
    save_raw_results(response, 'details_raw')
    return response.json()

def gplus_api(userid):
    """Google Plus API: returns json results,
    documentation: https://developers.google.com/+/api/latest/people/get"""
    base_url = 'https://www.googleapis.com/plus/v1/people/' + userid
    params = {'key' : API_KEY}
    response = requests.get(base_url, params=params)
    save_raw_results(response, 'gplus_raw')
    return response.json()

# Examples:
# overview = search_api("tokyo university")
# print json.dumps(overview, indent=2, ensure_ascii=False).encode('utf8')
# details = details_api(overview['results'][0]['place_id'], 'cn')
# print json.dumps(details, indent=2, ensure_ascii=False).encode('utf8')
# print json.dumps(gplus_api('107668880099887403676'), indent=2, ensure_ascii=False).encode('utf8')
