from shared import db
import models
import secure_random

class Session(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	session_id = db.Column(db.String(64))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = db.relationship('User', backref='sessions')

	def __init__(self, user_id):
		self.user_id = user_id
		self.session_id = secure_random.base64(64)

	def create(user_id):
		new_session = Session(user_id)
		db.session.add(new_session)
		db.session.commit()
		return new_session

	def destroy(session_id):
		db.session.delete(Session.query.filter_by(session_id=session_id).first())
		db.session.commit()

