# -*- coding: utf-8 -*-

from apis import *
from database import *

DB = 'from_google.db'
# langs = [ar, ja, bg, kn, bn, ko, ca, lt, cs, lv, da, ml, de, mr,
#          el, nl, en, no, eu, ro, fa, ru, fi, sk, fil, sl, fr, sr,
#          gl, sv, gu, ta, hi, te, hr, th, hu, tl, id, tr, it, uk,
#          iw, vi, pl, pt, es, eu]
langs = [en, jp, es, de, ko, ru, pt, nl, hi, ar, bg, ca, id, ml, te, vi, th, pl, it, iw]

def main_work(place_names):
    conn = sqlite3.connect(DB)
    for pn in place_names:
        # search place
        search_results = search_api(pn)
        # get details without specifying language
        details = details_api(search_results['results'][0]['place_id'])['result']
        # save details into the database
        store_place(details, conn)
        # save raw search results into the database
        # get details of the top place for each language

db_init(DB);
main_work(['tokyo university'])
