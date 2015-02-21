# -*- coding: utf-8 -*-

API_KEY = 'AIzaSyBBN84m4bDAzLnE1dhZ-QpDtAJcq-upOes'

import requests # Requests is recommended over urllib*
import json

def search_api(query, types=''):
    """Search API: returns json results,
    documentation: https://developers.google.com/places/documentation/search"""
    base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    params = {'key' : API_KEY, 'query' : query}
    if types != '':
        params['types'] = types
    response = requests.get(base_url, params=params)
    return response.json()

# print json.dumps(search_api("東京　大学"), indent=2)
