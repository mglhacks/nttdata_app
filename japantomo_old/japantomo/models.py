
import datetime
from japantomo import db

# User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)
    pw_hash = db.Column(db.String(120))
    country = db.Column(db.String(10))

    def __init__(self, username, email, pw_hash, country):
        self.username = username
        self.email = email
        self.pw_hash = pw_hash
        self.country = country

    def __repr__(self):
        return '<User %r>' % self.username

    def __getitem__(self, name): 
        return self.__getattribute__(name)

# Places
class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.Text)
    rating = db.Column(db.Integer)
    utc_offset = db.Column(db.Integer)
    user_ratings_total = db.Column(db.Integer)
    name = db.Column(db.String(80))
    photos = db.Column(db.Text)
    geometry = db.Column(db.Text)
    adr_address = db.Column(db.Text)
    place_id = db.Column(db.String(80))
    international_phone_number = db.Column(db.String(80))
    vicinity = db.Column(db.Text)
    reviews = db.Column(db.Text)
    url = db.Column(db.Text)
    address_components = db.Column(db.Text)
    formatted_address = db.Column(db.Text)
    types = db.Column(db.Text)
    icon = db.Column(db.Text)
    pref_id = db.Column(db.Integer)
    rurubu_pref_rank = db.Column(db.Integer)

    def __init__(self, website, rating, utc_offset, user_ratings_total, name, photos, geometry, adr_address, place_id, international_phone_number, vicinity, reviews, url, address_components, formatted_address, types, icon, pref_id, rurubu_pref_rank):
        self.website = website
        self.rating =  rating
        self.utc_offset = utc_offset
        self.user_ratings_total = user_ratings_total
        self.name = name
        self.photos = photos
        self.geometry = geometry
        self.adr_address = adr_address
        self.place_id = place_id
        self.international_phone_number = international_phone_number
        self.vicinity = vicinity
        self.reviews = reviews
        self.url = url
        self.address_components = address_components
        self.formatted_address = formatted_address
        self.types = types
        self.icon = icon
        self.pref_id = pref_id
        self.rurubu_pref_rank = rurubu_pref_rank

    def __repr__(self):
        return '<Place %r>' % self.name

    def __getitem__(self, name): 
        return self.__getattribute__(name)

# Names
class Placename(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer)
    name = db.Column(db.Integer)
    language = db.Column(db.Integer)

    def __init__(self, place_id, name, language):
        self.place_id = place_id
        self.name = name
        self.language = language

    def __repr__(self):
        return '<Placename %r>' % self.name

    def __getitem__(self, name): 
        return self.__getattribute__(name)

# Reviews
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    aspects_rating = db.Column(db.Integer) 
    aspects_type = db.Column(db.Text)
    language = db.Column(db.Integer) 
    text = db.Column(db.Text)
    author_name = db.Column(db.Text)
    author_url = db.Column(db.Text)
    time = db.Column(db.Integer)

    def __init__(self, place_id, rating, aspects_rating, aspects_type, language, text, author_name, author_url, time):
        self.place_id = place_id
        self.rating = rating
        self.aspects_rating = aspects_rating
        self.aspects_type = aspects_type
        self.language = language
        self.text = text
        self.author_name = author_name
        self.author_url = author_url
        self.time = time

    def __repr__(self):
        return '<User %r>' % self.username

    def __getitem__(self, name): 
        return self.__getattribute__(name)
