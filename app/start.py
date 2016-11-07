# this renders the home page which is start.html
from allImports import *
from flask_mail import Message
import json

@app.route("/<key>/<s_id>/<tag>/<value>", methods = ["GET"])
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
  return "Sucess!!!"                       


@app.route("/graph/<name>/<tag>")
def graph(name, tag):
  readings = (Reading.select()
                    .join(Sensor)
                    .where((Reading.tag == tag) & (Sensor.name==name)).limit(24))
                    
  return render_template("graph.html", readings = readings, tag = tag)
  
  
  
@app.route("/")
def main():
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
  
  
def not_mail():
  msg = Message("HELLo",
		sender="hunterr@berea.edu",
		recipients=["ramosmaciasg@berea.edu"])
  mail.send(msg)
  return "helllo"