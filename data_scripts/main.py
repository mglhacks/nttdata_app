# -*- coding: utf-8 -*-

from apis import *
from database import *
import codecs

# langs = [ar, ja, bg, kn, bn, ko, ca, lt, cs, lv, da, ml, de, mr,
#          el, nl, en, no, eu, ro, fa, ru, fi, sk, fil, sl, fr, sr,
#          gl, sv, gu, ta, hi, te, hr, th, hu, tl, id, tr, it, uk,
#          iw, vi, pl, pt, es, eu]
langs = ['en', 'ja', 'es', 'de', 'ko', 'ru', 'nl', 'ar', 'id', 'vi', 'th', 'pl', 'it']

def process_pref(pref_id):
    f_in = codecs.open('rurubu/%s.csv'%(pref_id), 'r', 'utf-8')
    pref_place_names = f_in.read().splitlines()
    for rurubu_pref_rank, pn in enumerate(pref_place_names, start=1):
        # search place
        search_results = search_api(pn)
        if len(search_results['results']) == 0:
            continue # no place found
        else:
            place_id = search_results['results'][0]['place_id']
            if get_place(place_id) != None:
                print "Place already exists"
                continue
        # get details of the top place for each language
        for l in langs:
            d = details_api(place_id, l)['result']
            if (l == 'en'):
                # save details into the database
                save_place_details(d, pref_id, rurubu_pref_rank)
            save_name(place_id, d['name'], l)
            if 'reviews' not in d:
                continue # No review
            for r in d['reviews']:
                if r.get('language') == l:
                    save_review(place_id, r)

db_init();
for pref_id in range(16, 48):
    process_pref(pref_id)
