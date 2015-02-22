# -*- coding: utf-8 -*-

import requests # Requests is recommended over urllib*

API_KEY = 'AIzaSyBBN84m4bDAzLnE1dhZ-QpDtAJcq-upOes'

def get_photo(photo_reference, maxwidth=0):
    """Places Text Search API: returns json results,
    documentation: https://developers.google.com/places/documentation/search"""
    base_url = 'https://maps.googleapis.com/maps/api/place/photo'
    params = {'key' : API_KEY, 'photo_reference' : photo_reference}
    if maxwidth != 0:
        params['maxwidth'] = maxwidth
    response = requests.get(base_url, params=params)
    # print response.content
    return response.content

# photo = get_photo('CvQB4gAAAGbRe84vNVLvmx7xOcICuZEH52iExU44q2S8ApfvByM74LnaDQehiC7zbcUrQn6tHtxR2TXlansviRUus28_AEU38r5JyiWNfMQddtCtIGyrdmKrXacsWkCp_iv6O0M6TAGE3AK71gG0fja_QJEdMvZb01_navrdb5yJXgPG08Sig81v1pWaZNw4ncBzJPsuapuIm_1u5gm2jbr351YkwRRZs5y7UpCLRPcWfhZ7XhMrkmPrcXJFG7mtip3mYcsAJEDTNDp7Q53xGBmKTs25-HOXmoHWN91uNA9nO88QXQulgApC5B7LCBPfGWzV5uCM_BIQhYBwVLVejUAq-Bb1kUeDuBoUSB4IFxVoWmMM3u2boZ8zjSZHtig')
# print photo
# dump(photo)
