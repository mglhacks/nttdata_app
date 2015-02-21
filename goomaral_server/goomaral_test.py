"""
2015/02/21
NTT Data Hackathon
Goo Maral Application
"""

from flask import Flask, request, send_from_directory
from flask import render_template
from flask_bootstrap import Bootstrap

# app creation
def create_app():
  app = Flask(__name__, static_url_path='')
  Bootstrap(app)
  return app
app = create_app()

# route for INDEX
@app.route("/")
def hello():
    return render_template('index.html')

# route for PROFILE
@app.route("/profile")
def profile():
	return render_template('profile.html')

# tests
@app.route('/hello/')
@app.route('/hello/<name>')
def hello_template(name=None):
	return render_template('hello.html', name=name)

@app.route('/test')
def test_page():
	return render_template('test.html')

# route for static js, css files
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)
@app.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory('static/fonts', path)
@app.route('/font-awesome/<path:path>')
def send_fontawesome(path):
    return send_from_directory('static/font-awesome', path)
@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('static/img', path)
@app.route('/less/<path:path>')
def send_less(path):
    return send_from_directory('static/less', path)

# main
if __name__ == "__main__":

	app.debug = True
	app.run(host="0.0.0.0")
