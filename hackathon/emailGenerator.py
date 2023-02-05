import smtplib
import random

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('getoutauthentication@gmail.com', 'jzrcrzjebtrsrqyg')

def email_gen(email):
   code = random.randrange(111111, 999999)
   msg = f'From: getoutauthentication@gmail.com\n To: {email}\nSubject: Verification Code\n\nYour Verification Code is: {code}.'
   server.sendmail('getoutauthentication@gmail.com', f'{email}', msg)
   return code
