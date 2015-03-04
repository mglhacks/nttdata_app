"""
2015/02/21
NTT Data Hackathon
Goo Maral Application
"""

"""
Important: this file is no longer used. Core file is app.__init__.py
"""

import os
# flask imports
from flask import Flask, request, session, url_for, redirect, render_template, abort, g, flash, _app_ctx_stack, jsonify, send_from_directory
from werkzeug import check_password_hash, generate_password_hash
from flask.ext.restful import reqparse, abort, Api, Resource
import json

import sqlite3

### Create app
# create our little application :)
app = Flask(__name__)
app.config.from_object('settings')
api = Api(app)


# user imports
from database_helper import *
import controllers


# main
if __name__ == "__main__":

    app.debug = True
    app.run(host="0.0.0.0")
