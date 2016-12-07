from peewee import *
import os
import datetime

# Create a database
from app.loadConfig import *
here      = os.path.dirname(__file__)
cfg       = load_config(os.path.join(here, 'config.yaml'))
mainDB    = SqliteDatabase(cfg['databases']['dev'])

# Creates the class that will be used by Peewee to store the database
class dbModel (Model):
  class Meta: 
    database = mainDB
    
"""
When adding new tables to the DB, add a new class here 
Also, you must add the table to the config.yaml file

Example of creating a Table

class tableName (dbModel):
  column1       = PrimaryKeyField()
  column2       = TextField()
  column3       = IntegerField()

For more information look at peewee documentation
"""

class Sensor (dbModel):
  '''Table holding sensor names'''
  _id            = PrimaryKeyField() #identify sensor
  name           = CharField() # civet

class Reading (dbModel):
  '''Table holding inventory information'''
  _id            = PrimaryKeyField() #what sensor
  sensor         = ForeignKeyField(Sensor, related_name="readings") # we need the sensor the reading belongs to
  tag            = CharField() #temp, humi, volt, etc...
  value          = FloatField()
  received       = DateTimeField(default=datetime.datetime.now())
  
  def __repr__(self):
    return str(self.value)
    
# this is a class because if it were yaml the server would have to be
# restarted in order for the changes to take place.
class Carrier( dbModel):
  """ table holding the people that will receive notification """
  name = CharField()
  email_string = CharField()
  
  def __repr__(self):
    return "{}".format(self.name)

# this is a class because if it were yaml the server would have to be
# restarted in order for the changes to take place.
class Manager( dbModel):
  """ table holding the people that will receive notification """
  name           = CharField()
  email          = CharField()
  phone          = CharField()
  mobile_carrier = ForeignKeyField(Carrier)
  
# this is a class because if it were yaml the server would have to be
# restarted in order for the changes to take place.
class AcceptableRange( dbModel ):
  """ holds the acceptable ranges that a sensor can have """
  _id          = PrimaryKeyField()
  sensor       = ForeignKeyField(Sensor) # so that sensor have own range
  tag          = CharField()
  high         = FloatField()
  low          = FloatField()