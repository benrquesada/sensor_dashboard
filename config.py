# email server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'notificationspmssthermostat'
MAIL_PASSWORD = 'pmss2000'

# administrator list
ADMINS = ['hunterr@berea.edu']

# Google Sheets Data

# Credentials are saved first time use of code with your google sheets information
# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
# Make sure to change your client_secret.json file according to your spreadsheet
CLIENT_SECRET = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python'

