# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup

handler = open('tmp.html').read()
soup = BeautifulSoup(handler)
spans = soup.findAll("span", { "class" : "mdLocation01SpotName" })

for span in spans:
    print span.text
