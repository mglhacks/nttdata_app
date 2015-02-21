# -*- coding: utf-8 -*-

import requests # Requests is recommended over urllib*
import codecs
from BeautifulSoup import BeautifulSoup

def get_places(content):
    soup = BeautifulSoup(content)
    elements = soup.find("div", {"id": "listBlock"}).findAll("h3")
    # print len(elements)
    return [e.text for e in elements]

def main_work():
    base_url = 'http://www.rurubu.com/ranking/index.aspx?'
    for pref_id in range(1, 48):
        f_out = codecs.open('rurubu/%s.csv'%(pref_id), 'w+', 'utf-8')
        for page in range(1, 6):
            params = {'KenCD' : pref_id, 'p' : page}
            response = requests.get(base_url, params=params)
            places = get_places(response.content)
            for p in places:
                f_out.write("%s\n"%p)
        f_out.close()

# main_work()
