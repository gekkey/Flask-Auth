from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__, static_folder='./static', static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/hackforward'
app.secret_key = 'totally a secret'
db = SQLAlchemy(app)
db.init_app(app)
db.create_all();
db.session.commit()
bcrypt = Bcrypt(app)
