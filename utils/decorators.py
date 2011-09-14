from google.appengine.api import users
from flask import redirect

def is_authenticated(f):
	
	def wrapper(*args, **kwargs):
		user = users.get_current_user()
		if user:
			return f(*args, **kwargs)
		else:
			return redirect(users.create_login_url("/"))

	return wrapper