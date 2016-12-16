from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtfpeewee.orm import model_form 
from models import Manager

class TemperatureRangeForm(FlaskForm):
    low_temp = IntegerField()
    high_temp = IntegerField()
    
ManagerForm = model_form(Manager, FlaskForm)