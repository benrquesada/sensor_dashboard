# this renders the home page which is start.html
from allImports import *
from flask_mail import Message
import json
import dweepy
from forms import ManagerForm

@app.route("/reading/<key>/<s_id>/<tag>/<value>", methods = ["GET"])
def save(key, s_id, tag, value):
  """Save Reading to database

  Keyword arguments:
  key -- a long integer that will identify a sensor
  tag -- the reading type temp, volt, humi, etc...
  value -- the actual reading 
  """
  if not int(key) in cfg['keys']: # don't continue if wrong key is given
    abort(403)
    
  sense = Reading(sensor = s_id ,tag = tag, value = value)
  sense.save()
  
  send_notification()
  
  send_dweet(s_id, tag, value)
  return "Sucess!!!"                       


@app.route("/graph/<name>/<tag>")
def graph(name, tag):
  """ Displays graph for a sensor """
  readings = (Reading.select()
                    .join(Sensor)
                    .where((Reading.tag == tag) & (Sensor.name==name)).limit(24))
                    
  return render_template("graph.html", readings = readings, tag = tag)
  
  
  
@app.route("/")
def main():
  """ Displays sensors """
  sensors = Sensor.select()
  sensor_dict = {}
  for sensor in sensors:
    sensor_dict[sensor.name] = {}
    for reading in sensor.readings:
      try:
        sensor_dict[sensor.name][reading.tag] = sensor_dict[sensor.name][reading.tag] + [reading.value]
      except KeyError:
        sensor_dict[sensor.name][reading.tag] = [reading.value]
  return render_template("data.html", cfg=cfg, sensors = sensor_dict)
  
  
def send_dweet(thing, dw_type, value):
  """ sends dweet with reading """
  dweepy.dweet_for(thing, {dw_type: int(value)})
  
@app.route("/managers", methods=["GET", "POST"])  
def manageManagers():
  """ form to change managers """
  managerForm = ManagerForm(request.form)
  managers    = Manager.select()
  print "function 1"
  if managerForm.validate_on_submit():
    print "this happened"
    name = managerForm.name.data
    email = managerForm.email.data
    phone = managerForm.phone.data
    mobile_carrier = managerForm.mobile_carrier.data
    Manager(name=name, email=email, phone=phone, mobile_carrier=mobile_carrier).save()
  return render_template("managers.html", managers=managers, managerForm=managerForm)
  
def send_notification():
  recipient_list = []
  managers = Manager.select()
  for manager in managers:
    phone_mail = "{}@{}".format(manager.phone, manager.mobile_carrier.email_string)
    recipient_list.append(phone_mail)
  msg = Message("HELLo",
		sender="hunterr@berea.edu",
		recipients=recipient_list)
  mail.send(msg)
  return "helllo"

@app.route("/sensor/options")
def notification_options():
  """the form that changes the sensor options """
  pass