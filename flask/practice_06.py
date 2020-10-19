from flask import Flask, render_template, request, url_for, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'hello'

@app.route('/login', methods=["POST", "GET"])
def login() :
    if request.method == 'POST' :
        name = request.form['name']
        session['user_name'] = name
        return redirect(url_for('user'))
    else :
        if 'user_name' in session:
                flash('You already logged in')
                return redirect(url_for('user'))
        else:
            return render_template('login.html')

@app.route('/user')
def user() :
    if 'user_name' in session :
      #  return f"You have typed name: {session['user_name']}"
        return render_template('user.html', name=session['user_name'])
    else :
        flash('You are not logged in')
        return redirect(url_for('login'))

@app.route('/logout')
def logout() :
    flash('You are logged out successfully...')
    session.pop("user_name", None)
    return redirect(url_for('login'))

if __name__ == '__main__' :
    app.run(debug=True)