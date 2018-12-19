import os
from ums import app
from ums import db
from ums.models import User

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
