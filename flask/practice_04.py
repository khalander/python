from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/login', methods=["POST", "GET"])
def login() :
    if request.method == 'POST' :
        name = request.form['name']
        return redirect(url_for('user', usr=name))
    else :
        return render_template('login.html')

@app.route('/user/<usr>')
def user(usr) :
    return f"You have typed name: {usr}"

if __name__ == '__main__' :
    app.run(debug=True)