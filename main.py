from flask import Flask
from flask import render_template, redirect

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.webapp.util import run_wsgi_app
from models.models import Offer
from jinja2 import environment
from utils import filters
from utils.filters import app
from utils.decorators import is_authenticated 


@app.route('/offer/<key>')
@is_authenticated
def offer_detail(key=None):
	offer = Offer.get(key)
	user = users.get_current_user()
	return render_template('detail.html', user=user, offer=offer)

@app.route('/')
def index():
	user = users.get_current_user()
	return render_template('index.html', user=user, offers=Offer.all())

@app.route('/auth')
def auth():
	user = users.get_current_user()
	if user:
		return 'Hello World! %s' % user.nickname()
	else:
		return redirect(users.create_login_url("/"))
	
@app.route('/logout')	
def logout():
	return redirect(users.create_logout_url("/"))
	
@app.route('/publish')
@is_authenticated
def publish():
	user = users.get_current_user()
	return render_template('publish.html', user=user)
	
def main():
	run_wsgi_app(app);

if __name__ == '__main__':
	main()