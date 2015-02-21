# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup

handler = open('tmp.html').read()
soup = BeautifulSoup(handler)
elements = soup.findAll("h3")

for e in elements:
    print e.text
