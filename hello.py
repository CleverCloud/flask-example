# -*- coding:utf-8 -*-

from flask import Flask, Response
app = Flask(__name__)

@app.route("/")
def headers():
    return request.headers.get("X-Forwarded-Protocol")

@app.route("/favicon.ico")
def favicon():
    resp = Response(status=200, mimetype='image/png')
    return resp

if __name__ == "__main__":
    app.run()
