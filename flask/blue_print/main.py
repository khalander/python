from flask import Flask, redirect, url_for

from admin.admin import admin

app = Flask(__name__)

app.register_blueprint(admin, url_prefix="/admin")

@app.route('/')
def home() :
    return "Welcome to home page"

if __name__ == '__main__' :
    app.run(debug=True)