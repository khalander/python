from flask import Flask, render_template, request, url_for, redirect, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(minutes=5)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class users(db.Model) :
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email) :
        self.name = name
        self.email = email



@app.route('/login', methods=["POST", "GET"])
def login() :
    if request.method == 'POST' :
        name = request.form['name']
        session['user_name'] = name

        foundUser = users.query.filter_by(name=name).first()
        if foundUser :
            session['email'] = foundUser.email
        else :
            usr = users(name, '')
            db.session.add(usr)
            db.session.commit()
        return redirect(url_for('user'))
    else :
        if 'user_name' in session:
                flash('You already logged in')
                return redirect(url_for('user'))
        else:
            return render_template('login.html')



@app.route('/user', methods=["POST", "GET"])
def user() :
    email = None
    if 'user_name' in session :
        name = session['user_name']
        if request.method == "POST" :
            email = request.form["email"]
            session['email'] = email
            foundUser = users.query.filter_by(name=name).first()
            foundUser.email = email
            db.session.commit()
            flash("Email was saved!!")
        else :
            if 'email' in session:
                email = session['email']
        return render_template('user.html', 
            name=session['user_name'],
            email = email
        )
    else :
        flash('You are not logged in')
        return redirect(url_for('login'))


@app.route('/view')
def view() :
    userList = users.query.all()
    return render_template("view.html", userList = userList)


@app.route('/logout')
def logout() :
    flash('You are logged out successfully...')
    session.pop("user_name", None)
    session.pop("email", None)
    return redirect(url_for('login'))

if __name__ == '__main__' :
    db.create_all()
    app.run(debug=True)