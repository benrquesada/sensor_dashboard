from peewee import *
import os

# Create a database
from app.loadConfig import *
here = os.path.dirname(__file__)
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

class Inventory (dbModel):
  '''Table holding inventory information'''
  i_id           = PrimaryKeyField()
  description    = TextField()
  size           = IntegerField()
  cost           = IntegerField()
  size_unit      = TextField()
  cost_per       = TextField()
  quantity       = IntegerField()
  
class Bow (dbModel):
  '''Table holding the types of bows and the inventory related'''
  b_id          = PrimaryKeyField()
  bow_type      = TextField()
  inventory     = ForeignKeyField(Inventory)    #ForeignKeyField(Related_table)
  design_name   = TextField()
  
class Customer (dbModel):
  '''Table holding customer information'''
  c_id          = PrimaryKeyField()
  first_name    = TextField()
  last_name     = TextField()
  email         = TextField()
  phone_number  = IntegerField()
  address       = TextField()

class Status(dbModel):
  s_id = PrimaryKeyField()
  status = CharField(unique = True)
  
class Order (dbModel):
  '''Table holding order information'''
  status        = ForeignKeyField(Status)
  number_of_bows= IntegerField()
  price         = IntegerField()
  created_date  = DateField()
  notes         = TextField()
  customer      = ForeignKeyField(Customer) # to customer class

