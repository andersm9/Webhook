from flask import Flask, request, abort

import requests
import json
import datetime as dt
import sys
import os
import getopt
from Keys import *

def send_it(token, room_id, message):

    header = {"Authorization": "Bearer %s" % token,
              "Content-Type": "application/json"}

    data = {"roomId": room_id,
            "text": message}

    return requests.post("https://api.ciscospark.com/v1/messages/", headers=header, data=json.dumps(data), verify=True)


app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        #print(type(request.json))
        print("The alert type is ")
        print(request.json["alertType"])
        print("   ")
        #if request.json["alertType"] == 'Settings changed':
        #print('call chaotbot here')
        send_it(token, teams_room, str(dt.datetime.now()) + "\n" + request.json["alertType"])
        #print(request.json)
        return '', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run(host= '0.0.0.0')

