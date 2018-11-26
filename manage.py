from flask import Flask
from flask import render_template

from flask_bootstrap import Bootstrap
import yaml

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def hello():
    return render_template('hello.html')

@app.route("/apps")
def apps():
    return render_template('apps.html')

@app.route("/publications")
def publications():
    pubs = yaml.load(open("publications.yaml").read())

    for pub in pubs['articles']:
        links = []
        pub['links'] = []
        if 'website' in pub:
            if pub['website'].startswith('http'):
                links.append((pub['website'], pub['website'][7:].rstrip('/')))
        if 'doi' in pub: links.append(('http://dx.doi.org/%s' % pub['doi'], 'DOI'))
        if 'pdf' in pub: links.append(('/static/pubs/%s' % pub['pdf'].replace(' ', '_'), 'PDF'))
        if 'git' in pub: links.append((pub['git'], 'GitHub'))

        for url,title in links:
            pub['links'].append("<a href='%s'>%s</a>" % (url, title))

    for pub in pubs['bookchapter']:
        links = []
        pub['links'] = []
        if 'website' in pub:
            if pub['website'].startswith('http'):
                links.append((pub['website'], pub['website'][7:].rstrip('/')))
        if 'doi' in pub: links.append(('http://dx.doi.org/%s' % pub['doi'], 'DOI'))
        if 'pdf' in pub: links.append(('/static/pubs/%s' % pub['pdf'].replace(' ', '_'), 'PDF'))

        for url,title in links:
            pub['links'].append("<a href='%s'>%s</a>" % (url, title))

    return render_template('publications.html', pubs=pubs)

@app.route("/about")
def about():
    return render_template('about.html')

