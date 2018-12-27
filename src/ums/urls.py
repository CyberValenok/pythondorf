from ums import app
from ums import db
from ums.models import User
from flask import abort, request, render_template, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def redirhome():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username=request.form['login']
        password=request.form['password']
        if not (username and password):
            flash("Field(s) is empy")
            return redirect(url_for('login'))
        else:
            username=username.strip(' ')
            password=password.strip(' ')

        user = User.query.filter_by(username=username).first()
        if username and bcrypt.check_password_hash(user.password, password):
            session[username] = True
            return redirect(url_for('userpage', username=username))
        else:
            flash("PRIVET POSHEL NAHUI, account does not exist!")
    return render_template('login.html')

@app.route('/home/<username>/')
def userpage(username):
    if not session.get(username):
        abort(401)
    return render_template('userpage.html', username=username)

@app.route('/signup', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users():
    if request.method== 'POST':
        username=request.form['login'].strip(' ')
        password=request.form['password'].strip(' ')

        pass_hash=bcrypt.generate_password_hash(password)

        user=User(username=username, password=pass_hash)
        db.create_all()
        db.session.add(user)
        db.session.commit()
    return render_template('registration.html')
