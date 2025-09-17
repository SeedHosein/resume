from flask import Flask, request, redirect, send_from_directory, url_for, render_template

app = Flask(
        __name__,
        static_folder='static',
        )

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

if __name__ == '__main__':
    app.run(debug=False)