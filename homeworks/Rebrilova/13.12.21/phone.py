#import os
from twilio.rest import Client
import sys

toDo = str(sys.argv[1])
print(toDo)

account_sid = 'ACa19f70c845f7018e90c4ba2311a1e70d'
auth_token = '4dc3d23d2ed3e66fb158c4e2e6e19781'


def call_joke(phone_number):
    client = Client(account_sid, auth_token)
    call = client.calls.create(
        twiml='<Response><Say voice="alice">' + toDo + '</Say></Response>',
        to=phone_number,
        from_='+16816411334')
    return call.sid


call_joke('+79112871146')