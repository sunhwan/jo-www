from flask import Flask
from flask import render_template

from flask_bootstrap import Bootstrap
import yaml
import markdown

app = Flask(__name__)
Bootstrap(app)

md = markdown.Markdown(extensions = ['meta'])

@app.route("/")
def hello():
    posts = yaml.load(open("entries/entries.yaml").read())
    for post in posts:
        post['content'] = md.convert(open("entries/%s" % post['filename']).read())
    return render_template('posts.html', posts=posts)

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

