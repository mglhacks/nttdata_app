# -*- coding: utf-8 -*-

from apis import *
from database import *

# langs = [ar, ja, bg, kn, bn, ko, ca, lt, cs, lv, da, ml, de, mr,
#          el, nl, en, no, eu, ro, fa, ru, fi, sk, fil, sl, fr, sr,
#          gl, sv, gu, ta, hi, te, hr, th, hu, tl, id, tr, it, uk,
#          iw, vi, pl, pt, es, eu]
langs = ['en', 'jp', 'es', 'de', 'ko', 'ru', 'pt', 'nl', 'hi', 'ar', 'bg', 'ca', 'id', 'ml', 'te', 'vi', 'th', 'pl', 'it', 'iw']

def main_work(place_names):
    for pn in place_names:
        # search place
        search_results = search_api(pn)
        if len(search_results['results']) == 0:
            return # no place found
        else:
            place_id = search_results['results'][0]['place_id']
        # get details of the top place without specifying language
        details = details_api(place_id)['result']
        # save details into the database
        save_place_details(details)
        # get details of the top place for each language
        for l in langs:
            d = details_api(place_id, l)['result']
            save_place_details(d)
            save_name(place_id, d['name'], l)
            for r in d['reviews']:
                if r['language'] == l:
                    save_review(place_id, r)

db_init();
main_work(['tokyo tower'])
