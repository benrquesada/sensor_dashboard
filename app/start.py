# this renders the home page which is start.html
from allImports import *
@app.route("/<key>/<id>/<tag>/<value>", methods = ["GET"])
def start(key, id, tag, value):
  print ("Key: {0} ID: {1} Tag: {2} Value: {3}".format(key, id, tag, value))
  return "Sucess!!!"                       
