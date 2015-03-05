# -*- coding: utf-8 -*-

"""Utility methods for conversing with various APIs"""

import requests # Requests is recommended over urllib*

API_KEY = 'AIzaSyBBN84m4bDAzLnE1dhZ-QpDtAJcq-upOes'

def get_photo_src(photo_reference, maxwidth=300):
    """Returns image src value either as a relative path or base64  value,
    API documentation: https://developers.google.com/places/documentation/photos"""
    base_url = 'https://maps.googleapis.com/maps/api/place/photo'
    params = {'key' : API_KEY, 'photoreference' : photo_reference, 'maxwidth': maxwidth}
    response = requests.get(base_url, params=params)
    if response.headers.get('content-type') == None:
        return ''
    else:
        return 'data:%s;base64,%s'%(
            response.headers.get('content-type'),\
            response.content.encode("base64").rstrip('\n'))
