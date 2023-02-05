from twilio.rest import Client
import database

# Your Account SID from twilio.com/console
account_sid = "ACb70cf4004c25e63a1e5ef11e71eb0f02"
# Your Auth Token from twilio.com/console
auth_token  = "2a95074da160447c36a4448f3ada65f8"
client = Client(account_sid, auth_token)


def message(num_o, num, name):
    message = client.messages.create(
        to=f"+1{num_o}", 
        from_="+17046669049",
        body=f"Hey! You're buddy is ready! Their name is {name} and their phone number is {num}.")
    return message
