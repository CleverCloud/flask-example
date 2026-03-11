import platform

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world!"


@app.route("/headers")
def headers():
    return "<br/>".join(
        [f"{key} => {value}" for (key, value) in request.headers.items()]
    )


@app.route("/pyver")
def pyver():
    return platform.python_version()
