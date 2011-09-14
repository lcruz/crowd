from google.appengine.ext import db

class Offer(db.Model):	
	owner = db.UserProperty()
	title = db.StringProperty()
	description = db.StringProperty(multiline=True)
	date = db.DateTimeProperty(auto_now_add=True)

