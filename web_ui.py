import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')
app.run(host='127.0.0.1', port=8000)