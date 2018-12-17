import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.Boolean)

    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.is_active = True

@app.route('/')
def index():
    db.create_all()
    user = User('admin', '123456789')
    db.session.add(user)
    db.session.commit()
    return 'index'

@app.route('/<string:username>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users(username):
    if request.method == 'GET':
        return 'user'
