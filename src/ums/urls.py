import os
from ums import app
from ums import db
from ums.models import User
#from ums.forms import LoginForm
from flask import request, render_template

@app.route('/login')
def login():
    return render_template('log.html')


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users():
    if request.method== 'POST':
        user1= User(request.form['login'],request.form['password'])
        db.create_all()
        db.session.add(user1)
        db.session.commit()
    return render_template('reg.html')
