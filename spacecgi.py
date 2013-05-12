#!/usr/bin/python2

# Please change the token before deploying.

import cgi
import json
import sys
from time import time

print "Content-type: text/plain"
print ""

args = cgi.FieldStorage()
if not "token" in args.keys():
    print "Pls authenticate"
    sys.exit(0)

try:
    data_file = open("data.json", "r")
    data = json.loads(data_file.read())
    data_file.close()

except:
    print ("Error opening files")
    sys.exit(0)

if str(args["token"].value) != "lolnope":
    print "Fak u"
    sys.exit(0)

if not "update_device_count" in args.keys():
    print "What do you want to do?"
    sys.exit(0)

# change data
if int(args["update_device_count"].value) > 0:
    data["open"] = True
else:
    data["open"] = False

data["lastchange"] = int(time())

# save data
try:
    datafile = open("data.json", "w")
    datafile.write(json.dumps(data))
    datafile.close()
    print "This was a triumph"
except:
    print "cannot save changes"
