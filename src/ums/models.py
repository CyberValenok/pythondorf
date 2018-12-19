
from ums import db


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
