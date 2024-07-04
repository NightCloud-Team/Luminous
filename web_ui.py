import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/software')
def software():
    return flask.render_template('software.html')


@app.route('/SpecialThanks')
def SpecialThanks():
    return flask.render_template('SpecialThanks.html')


@app.route('/website')
def website():
    return flask.render_template('website.html')


app.run(host='127.0.0.1', port=8000)
