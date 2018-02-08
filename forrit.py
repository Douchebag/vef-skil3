from bottle import route, run, template, static_file, request, error
import os

@route('/')
def index():
    return "<a href='/a'>Liður a</a> <a href='/b'>Liður b</a>"
@route('/a')
def a():
    return template('a')
@route("/sida/<id>")
def sida(id):
    return template('sida', kt=id)
@route("/b")
def b():
    return template('b')

@route("/static/<filename>")
def server_static(filename):
    return static_file(filename, root='./css')

@route("/frett/<id>")
def frett(id):
    return template(id)

@error(404)
def error404(error):
    return "<h1>Þessi síða fannst ekki</h1>"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
