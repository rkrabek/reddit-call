# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
# Get these credentials from http://twilio.com/user/account
account_sid = "XXXX"
auth_token = "XXXX"
client = TwilioRestClient(account_sid, auth_token)
# Make the call
call = client.calls.create(to="+xxx",  # Any phone number
                           from_="+xxx", # Must be a valid Twilio number
                           url= "http://www.dropbox.com/s/monap5wnp61hcoq/response.xml?dl=1")
print call.sid