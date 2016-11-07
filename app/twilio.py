# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
import twilio_credentials
client = TwilioRestClient(twilio_credentials.account_sid, twilio_credentials.auth_token)

message = client.messages.create(to="+12316851234", from_="+15555555555", # need twilio phone number
                                     body="Hello there!")