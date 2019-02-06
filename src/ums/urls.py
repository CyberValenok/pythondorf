from ums import app
from ums import db
from ums.models import User
from flask import abort, request, render_template, redirect, url_for, session, flash
from flask import jsonify
from ums import bcrypt
from sqlalchemy.exc import IntegrityError, OperationalError

@app.route('/')
def redirhome():
    return redirect(url_for('home'))

@app.route('/home')
def home(username=None):
    if session.get('username'):
        username = session['username']
        flash('Your personal page, Tik-toha')
        return redirect(url_for('userpage', username=username))
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if session.get("username"):
        return redirect(url_for('home'))
    if request.method == 'POST':
        username=request.form['login']
        password=request.form['password']
        if not (username and password):
            flash('Field(s) is empy!')
            return redirect(url_for("login"))
        else:
            username=username.strip(' ')
            password=password.strip(' ')
        try:
            user = User.query.filter_by(username=username).first()
        except OperationalError:
            flash("DataBase does not created, toha. Create new users to activate DB.")
            return redirect(url_for('users'))
        if user and bcrypt.check_password_hash(user.password, password):
            session['username'] =  username
            return redirect(url_for('userpage', username=username))
        else:
            flash('PRIVET POSHEL NAHUI, account does not exist!')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/home/<username>/')
def userpage(username):
    if not session.get('username'):
        return redirect(url_for('login'))
    return render_template('userpage.html', username=username)

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("TOHA, successfully logout")
    return redirect(url_for('home'))

@app.route('/signup', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users():
    if request.method== 'POST':
        username=request.form['login'].strip(' ')
        password=request.form['password'].strip(' ')
        if not (username and password):
            flash('Field(s) is empty!')
            return redirect(url_for('users'))
        pass_hash=bcrypt.generate_password_hash(password)

        user=User(username=username, password=pass_hash)
        db.create_all()
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            flash("Toha, ne obmanyvai! Account {username} been created".format(username=username))
            return redirect(url_for("users"))
        if session.get('username'):
            flash('Account successfull created!')
            return redirect(url_for('home'))
        flash("KRASAVA!!!!!!!!, zahodi")
        return redirect(url_for("login"))
    return render_template('registration.html')

@app.route('/userlist')
def userlist():
    return render_template('userlist.html')
