#!/usr/bin/env python

from __future__ import print_function
from future import standard_library

standard_library.install_aliases()
import configparser
import sys

import requests
from flask import Flask, request, render_template, abort

application = Flask(__name__)


@application.route("/")
def hello():
    print("Print alive message", file=sys.stderr) 
    return "I'm alive.", 200

@application.route("/post", methods=['POST'])
def post():
    if request.method == 'POST': 
        print("Result: \n%s\n" % request.data, file=sys.stderr)
        return "Result: \n%s\n" % request.data, 200
    else:
        abort(400)

if __name__ == '__main__':
    application.run(host="0.0.0.0", port=8080)

# port 8080 is needed for s2i in openshift
