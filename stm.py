from twilio  import rest

# Your Account SID from twilio.com/console
account_sid = "AC7XXXXX"
# Your Auth Token from twilio.com/console
auth_token  = ""

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+63XXXXXXXX", 
    from_="+193XXXXXX",
    body="Another test from cjpesco?")

print(message.sid)