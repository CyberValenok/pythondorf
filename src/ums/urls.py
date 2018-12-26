from ums import app
from ums import db
from ums.models import User
from flask import abort, request, render_template, redirect, url_for, session, flash

@app.route('/')
def redirhome():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        UsNa=request.form['login']
        Pass=request.form['password']
        if not (UsNa and Pass):
            flash("Field(s) is empy")
            return redirect(url_for('login'))
        else:
            UsNa=UsNa.strip(' ')
            Pass=Pass.strip(' ')
        user = User.query.filter_by(UsNa=username).first()
        if UsNa and check_pass(user.password, Pass):
            session[UsNa] = True
            return redirect(url_for('us_strt', UsNa=username))
        else:
            flash("PRIVET POSHEL NAHUI, Account does not exist!")
    return render_template('log.html')
@app.route('/user/<UsNa>/')
def us_strt():
    if not session.get(UsNa):
        abort(401)
    return render_template('userpage.html')
@app.route('/signup', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users():
    if request.method== 'POST':
        reg = User(request.form['login'].strip(' '), request.form['password'].strip(' '))
        db.create_all()
        db.session.add(reg)
        db.session.commit()
    return render_template('reg.html')
