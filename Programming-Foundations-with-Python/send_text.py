from twilio.rest import TwilioRestClient # import from outside library
# from twilio import rest


account_sid = "ACd926951572ae9fbf5ddff8fb01af7d22" # Your Account SID from www.twilio.com/console
auth_token  = "fad9b988b1a3926caa2fd6bfcc8578c9"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)
# client = rest.TwilioRestClient()
 
message = client.messages.create(
    body="I'm Punellissia", #text content
    to="+13478200166",    # Replace with your phone number
    from_="+16468671861") # Replace with your Twilio number

print(message.sid)
