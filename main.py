from flask import Flask, session, request, g, send_file, redirect, render_template, url_for
from shared import app, db, bcrypt
from models import *

# user auth
@app.before_request
def verify_user():
	if 'session_id' in session:
		try:
			g.user = Session.query.filter_by(
					session_id=session['session_id']).first().user.username
		except AttributeError:
			session.pop('session_id')
	else:
		g.user = None

# serve app
@app.route("/")
def index():
	return render_template('index.html')

@app.route("/<path:path>")
def static_file(path):
	return send_from_directory('/static', path)

@app.route("/login", methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		if g.user:
			return redirect(url_for("index"))
		else:
			return send_file('./static/login.html')
	elif request.method == 'POST':
		user = User.login(request.form['username'], request.form['password'])
		if user:
			g.user = user.username
			session['session_id'] = Session.create(user.id).session_id
			return redirect(url_for("index"))
		else:
			return redirect(url_for("login"))

@app.route("/signup", methods=['GET', 'POST'])
def signup():
	if request.method == 'GET':
		if g.user:
			return redirect(url_for("index"))
		else:
			return send_file('./static/signup.html')
	elif request.method == 'POST':
		try:
			user = User.create(request.form['username'], request.form['password'])
			g.user = user.username
			return redirect(url_for("index"))
		except:
			return send_file('./static/signup.html')

@app.route("/logout")
def logout():
	current_session = session.pop('session_id', None)
	if current_session:
		Session.destroy(current_session)
	return redirect(url_for("index"))

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
