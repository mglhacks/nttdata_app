from flask import Blueprint, render_template

rankings = Blueprint('rankings', __name__, url_prefix='/rankings')


@rankings.route('/')
def index():

    return render_template('rankings/index.html')