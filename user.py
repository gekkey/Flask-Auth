from session import Session
from shared import db, bcrypt
import models

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(255), unique=True)
	password = db.Column(db.String(255))

	def __init__(self, username, password):
		self.username = username
		self.password = bcrypt.generate_password_hash(password)

	def create(username, password):
		user = User(username, password)
		db.session.add(user)
		db.session.commit()
		return user

	def login(username, password):
		user = User.query.filter_by(username=username).first()
		if bcrypt.check_password_hash(user.password, password):
			return user
