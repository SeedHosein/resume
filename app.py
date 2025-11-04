from flask import Flask, Response, request, redirect, url_for, render_template, json
from flask_sitemapper import Sitemapper
from whitenoise import WhiteNoise

sitemapper = Sitemapper()

app = Flask(
        __name__,
        static_folder='static',
        static_url_path="/"
        )

app.wsgi_app = WhiteNoise(app.wsgi_app, root='static', prefix='/')
sitemapper.init_app(app)


@sitemapper.include(changefreq="weekly", priority=1.0)
@app.route("/fa")
@app.route("/")
def index():
    return redirect(url_for('resume_fa'))

@sitemapper.include(changefreq="daily", priority=0.9)
@app.route("/fa/resume")
def resume_fa():
    with open("./data.json", "r") as f:
        data = json.load(f)

    return render_template('resume.html', **data)


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