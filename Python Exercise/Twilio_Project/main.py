from twilio.rest import Client
import keys

client = Client(keys.accounts_id, keys.auth_token)
client = Client(keys.accounts_id, keys.auth_token)

message = client.messages.create(
    body="Hello Good Evening, Message from Chandhan!!",
    from_=keys.twilio_number,
    to=keys.my_phone_number,
)
print(message.body)
