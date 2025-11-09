import os
from flask import Flask, Response, abort, request, redirect, send_from_directory, url_for, render_template, json
from flask_sitemapper import Sitemapper
from werkzeug.utils import safe_join
from whitenoise import WhiteNoise

sitemapper = Sitemapper()

app = Flask(
        __name__,
        static_folder='static',
        )
sitemapper.init_app(app)


@sitemapper.include(changefreq="weekly", priority=1.0)
@app.route("/")
def index():
    return redirect(url_for('resume_en'))

@app.route("/en/")
def redirect_en():
    return redirect(url_for('resume_en'))

@app.route("/fa/")
def redirect_fa():
    return redirect(url_for('resume_fa'))

@sitemapper.include(changefreq="daily", priority=0.9)
@app.route("/fa/resume/")
def resume_fa():
    with open("./data-fa.json", "r") as f:
        data = json.load(f)

    return render_template('resume-fa.html', url_external=url_for('resume_fa', _external=True), **data)

@sitemapper.include(changefreq="daily", priority=0.9)
@app.route("/en/resume/")
def resume_en():
    with open("./data-en.json", "r") as f:
        data = json.load(f)

    return render_template('resume-en.html', url_external=url_for('resume_en', _external=True), **data)


@app.route("/sitemap.xml")
def sitemap():
  return sitemapper.generate()

@app.route('/robots.txt')
def noindex():
    robots_txt = f'''
User-agent: *
Allow: /
Disallow: /404/

Sitemap: { url_for('sitemap', _external=True) }
    '''
    r = Response(response=robots_txt, status=200, mimetype="text/plain")
    r.headers["Content-Type"] = "text/plain; charset=utf-8"
    return r


if __name__ == '__main__':
    app.run(debug=False)