Welcome to the PMSSnotification DashBoard

#setup#
1. run ```source setup.sh```
2. run ```python create_db.py```
3. run ```python app.py```

#sending data#
All sensor data can be sent to
baseurl.com/reading/&lt;key&gt;/&lt;s_id&gt;/&lt;tag&gt;/&lt;val&gt;

where:
* key - the key that the server is expecting (this is done so that someone can't stumble upon the site and mess data)
* s_id - the name of the sensor
* tag - reading type; temp, humi, volt
* val - the value of the reading

# viewing data #
all data can be viewed entering the base url

Here there will be several sensors with readings on them. 
New sensors will be automatically displayed on this page
The user can click on a sensor to get the last 24 readings in graph form

