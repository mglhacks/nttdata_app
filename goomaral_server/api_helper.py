# -*- coding: utf-8 -*-

import requests # Requests is recommended over urllib*
import codecs

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

# print get_photo_src('CvQB4gAAAGbRe84vNVLvmx7xOcICuZEH52iExU44q2S8ApfvByM74LnaDQehiC7zbcUrQn6tHtxR2TXlansviRUus28_AEU38r5JyiWNfMQddtCtIGyrdmKrXacsWkCp_iv6O0M6TAGE3AK71gG0fja_QJEdMvZb01_navrdb5yJXgPG08Sig81v1pWaZNw4ncBzJPsuapuIm_1u5gm2jbr351YkwRRZs5y7UpCLRPcWfhZ7XhMrkmPrcXJFG7mtip3mYcsAJEDTNDp7Q53xGBmKTs25-HOXmoHWN91uNA9nO88QXQulgApC5B7LCBPfGWzV5uCM_BIQhYBwVLVejUAq-Bb1kUeDuBoUSB4IFxVoWmMM3u2boZ8zjSZHtig', 300)
