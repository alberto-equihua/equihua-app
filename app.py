from crypt import methods
from flask import Flask, render_template, request, flash, session

app = Flask(__name__)
app.secret_key = "1aB&80hFD"

@app.route("/")
def index():
    flash("What's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["GET", "POST"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", greet to see you!")
    return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run()