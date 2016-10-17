# WARNING: NOT FOR USE IN PRODUCTION AFTER REAL DATA EXISTS!!!!!!!!!!!!!!!!!!!!!!
'''
This script creates the database tables in the SQLite file. 
Update this file as you update your database.
'''
import os, sys
import importlib

# Don't forget to import your own models!
from app.models import *

conf = load_config('app/config.yaml')

sqlite_dbs  = [ conf['databases']['dev']
                # add more here if multiple DBs
              ]

# Remove DBs
for fname in sqlite_dbs:
  try:
    print ("Removing {0}.".format(fname))
    os.remove(fname)
  except OSError:
    pass

# Creates DBs
for fname in sqlite_dbs:
  if os.path.isfile(fname):
    print ("Database {0} should not exist at this point!".format(fname))
  print ("Creating empty SQLite file: {0}.".format(fname))
  open(fname, 'a').close()
  

def class_from_name (module_name, class_name):
  # load the module, will raise ImportError if module cannot be loaded
  # m = __import__(module_name, globals(), locals(), class_name)
  # get the class, will raise AttributeError if class cannot be found
  c = getattr(module_name, class_name)
  return c
    
"""This file creates the database and fills it with some dummy run it after you have made changes to the models pages."""
def get_classes (db):
  classes = []
  for str in conf['models'][db]:
    print ("\tCreating model for '{0}'".format(str))
    c = class_from_name(sys.modules[__name__], str)
    classes.append(c)
  return classes

  
mainDB.create_tables(get_classes('mainDB'))

# Adding dummy data
inventory1 = Inventory(  description = "plank of wood",
                size  = 4,
                cost  = 14.30,
                size_unit = "ft",
                cost_per = "set",
                quantity = 5
             )
inventory1.save()
             
inventory2 = Inventory(  description = "steel bolt",
                size  = 17,
                cost  = 2.67,
                size_unit = "in",
                cost_per = "inch",
                quantity = 23
             )
inventory2.save()
             
bow1= Bow ( bow_type= "front",
           inventory= inventory1.i_id,
           design_name= "Gothic"
           )
bow1.save()
           
bow2= Bow ( bow_type= "back ",
           inventory= inventory2.i_id,
           design_name= "Gothic"
           )
           
bow2.save()
           
customer1 =  Customer ( first_name  = "John",
                       last_name   = "Doe",
                       email       = "johndoe@example.com",
                       phone_number = 8738432344,
                       address     = "123 sample address, Somewhere, 23234"
                      )
customer1.save()

customer2 =  Customer ( first_name  = "Jane",
                       last_name   = "Doe",
                       email       = "janedoe@example.com",
                       phone_number = 8779872344,
                       address     = "123 sample address, Somewhere, 23234"
                      )
customer2.save()

status1 = Status ( status        = "Confirmed",
                 )
status1.save()

status2 = Status ( status        = "Pending Delivery",
                 )
status2.save()
                  
order1 = Order ( status        = status1.s_id,
                  number_of_bows= 12,
                  price         = 2200,
                  created_date  = "09/05/1995",
                  notes         = "Wanted Additional Door Installed",
                  customer      = customer1.c_id
                )
order1.save()

order2 = Order ( status        = status2.s_id,
                  number_of_bows= 20,
                  price         = 3100,
                  created_date  = "02/27/1997",
                  notes         = "THIS IS A NOTE",
                  customer      = customer2.c_id
                )
order2.save()