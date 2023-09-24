from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/maze')
def maze():
    return render_template('maze.html')

app.run(debug=True)