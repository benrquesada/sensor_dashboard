<<<<<<< Updated upstream
=======
# this renders the home page which is start.html
from allImports import *
from flask_mail import Message
@app.route("/<key>/<id>/<tag>/<value>", methods = ["GET"])
def start(key, id, tag, value):
  print ("Key: {0} ID: {1} Tag: {2} Value: {3}".format(key, id, tag, value))
  
  return "Sucess!!!"                       


@app.route("/mail")
def not_mail():
  msg = Message("HELLo",
		sender="hunterr@berea.edu",
		recipients=["ramosmaciasg@berea.edu"])
  mail.send(msg)
  return "helllo"
>>>>>>> Stashed changes
