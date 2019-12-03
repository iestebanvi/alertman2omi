#!/usr/bin/env python

from __future__ import print_function
from future import standard_library

standard_library.install_aliases()
import sys
import os

import requests
from flask import Flask, request, render_template, abort

application = Flask(__name__)

try:
    post_url = os.environ.get("OMI_URL", "http://omireceiver.alertman2omi.svc:8080/post")
    ini_category = os.environ.get("OMI_CATEGORY", "incident")
    ini_affectedCI = os.environ.get("OMI_CI", "OpenShift")
except Exception as ex:
    print('Something is wrong with config env vars OMI_URL, OMI_CATEGORY, OMI_CI: {}'.format(ex))
    sys.exit(1)


@application.route("/")
def hello():
    return "I'm alive.", 200

@application.route("/test", methods=['POST'])
def internal_test():
    if request.method == 'POST': 

        print("Result: \n%s\n" % request.data)
        return "ok", 200
    else:
        abort(400)

@application.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':

        alert = request.json
        print("Incoming JSON: %s\n" % alert)

        msgs = "MESSAGES: "
        names = ""
        alnames = {}
        components = ""
        sev = "none"

        for al in alert['alerts']:
            if al['labels']['alertname'] not in alnames:
                alnames[ al['labels']['alertname'] ] = 1
            else:
                alnames[ al['labels']['alertname'] ] += 1
            msgs = msgs + al['annotations']['message'] + " | "
            if 'namespace' in al['labels']:
                components = components + al['labels']['namespace']
                if 'pod' in al['labels']:
                    components = components + "." + al['labels']['pod']
                components = components + " | "

            if  al['labels']['severity'] == 'critical':
                sev = 'critical'
            elif al['labels']['severity'] == 'warning' and sev != 'critical' :
                sev = 'warning'            

        for n in alnames:
            names = names + n
            if alnames[n] > 1:
                names = names + " x" + str(alnames[n])
            names = names + " | "
            
        omi = render_template('template.xml',
                              title=names[:-3],
                              description=msgs[:-3],
                              severity=sev,
                              node=components[:-3],
                              category=ini_category,
                              affectedCI=ini_affectedCI
                              )

        headers = {
            'Content-type': 'text/xml',
        }

        print ("Send to omi %s\n%s\n%s"% (post_url,headers,omi))
        response = requests.post(post_url, headers=headers, data=omi)
        return '', response.status_code
    else:
        abort(400)


if __name__ == '__main__':
    application.run(host="0.0.0.0", port=8080, debug=True)

# port 8080 is needed for s2i in openshift
 
