from flask import Flask, request, redirect, send_from_directory, url_for, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for('resume_fa'))

@app.route("/fa")
def resume_fa():
    data = {
        "name": "سیدحسین موسوی دهاقانی",
        "age": "20",
        "about": "",
        "skills": [
            "",""
            ],
        
    }
    return render_template('index.html', **data)

@app.route('/static/<path:path>')
def send_report(path):
    # Using request args for path will expose you to directory traversal attacks
    return send_from_directory('static', path)