#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from json import load, loads
from os import chdir as workspace
from os.path import join

from flask import send_from_directory, render_template
from flask import Flask, redirect, request

from make import *

app = Flask("sorry")
# Modify according to personal circumstances.
workspace("/home/sxy/Scripts/sorry/")


@app.route("/favicon.ico")
def favi():
    return send_from_directory(
        join(app.root_path, "static/img"), "favicon.ico",
        mimetype="image/vnd.microsoft.icon"
    )


@app.route("/")
def main():
    return redirect("/sorry")


@app.route("/<type>", methods=['GET', 'POST'])
def show(type="sorry"):
    app.logger.debug("Request GIF type:  " + type)
    with open("static/config.json", "r") as fp: return render_template(
        "index.html", type=type, contents=load(fp)
    )


@app.route("/<type>/make", methods=['POST'])
def make(type="sorry"):
    path = make_gif(type, {
        int(k): v for k, v in loads(request.get_data()).items()
    })
    app.logger.debug("Target file path:  " + path)
    return path if path else 'static/img/erro.png'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888, debug=True)
