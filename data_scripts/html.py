# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup

handler = open('tokyo.html').read()
soup = BeautifulSoup(handler)
h1s = soup.findAll("h1", { "class" : "card__content__title js-prerender-title" })

for h1 in h1s:
    print h1.text
