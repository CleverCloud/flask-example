# -*- coding:utf-8 -*-

import subprocess
from flask import Flask, Response, request
app = Flask(__name__)

@app.route("/")
def headers():
    return '<br/>'.join(['%s => %s' % (key, value) for (key, value) in request.headers.items()])

@app.route("/favicon.ico")
def favicon():
    resp = Response(status=200, mimetype='image/png')
    return resp

@app.route("/tag")
def tag():
    p = subprocess.Popen(['git', 'describe', '--tags', '--abbrev=0'], stdout=subprocess.PIPE)
    p.wait()
    return p.stdout.read()

if __name__ == "__main__":
    app.run()
