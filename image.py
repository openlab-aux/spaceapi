import cgi
import json

data = json.loads(open("data.json").read())

if data["open"]:
    f = open("openlab-open.png")
else:
    f = open("openlab-closed.png")

print "Content-Type: image/png"
#print "Content-Length: %i" % len(f)
print ""
print f.read()
