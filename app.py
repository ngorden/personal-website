from flask import Flask, redirect, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return redirect('/home/')


@app.route('/favicon.ico/')
def favicon():
    return 'hello world'


@app.route('/<string:page_name>/')
def page_render(page_name: str):
    return render_template('content/%s.html' % page_name)


if __name__ == '__main__':
    app.run()
