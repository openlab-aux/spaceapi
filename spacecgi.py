#-*- coding: utf-8 -*-

import json
import cgi
import cgitb
cgitb.enable(display=0, logdir="/tmp/")
from time import time

args = cgi.FieldStorage()

DATAPATH = "/var/www/data.json"
TOKENPATH = "/var/www/token"

token = open(TOKENPATH,"r").read()
if token == args["token"].value:
    data_file = open(DATAPATH,"r")
    data = json.loads(data_file.read())
    data_file.close()
    for key, field in args.items():
        if key == "update_device_count":
            data["open"] = field.value > 0
        # elif key == "some_other_command":
        #   do stuff
        else:
            pass #ignore invalid commands
    data["lastchange"] = int(time())
    data_file = open(DATAPATH,"w")
    data_file.write(json.dumps(data))
    print "Content-Type: text/plain"
    print
    print "Success!"
else:
    print "Content-Type: text/plain"
    print
    print "Fak u dolan, y u do tis dolan?"
