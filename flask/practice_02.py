from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/user/<name>')
def user(name) :
    return f"hello, {name}"

@app.route('/admin/')
def admin() :
    return redirect(url_for('user', name='Admin'))

@app.route('/home')
def home () :
    # return render_template('index.html', content='Mufeez', age='7')
    return render_template('index.html', content= ['Mufeez', 'Rabia', 'Fathima'])

if __name__ == '__main__' :
    app.run(debug=True)