import os
import imghdr
import smtplib
from debugger import debug
import urllib.request as urllib2
from email.message import EmailMessage
import matplotlib.pyplot as plt

def internet_on(): #makes sure that there is an internet connection
    try:
        urllib2.urlopen('https://www.google.com/', timeout = 1)
        return True
    except urllib2.URLError as err:
        return False

def twoFactorAuthentification(code):
    pass

def sendCodeEmail(code, data, email = 'gotten'):
    password = data[code][0]["password"]
    name = data[code][0]["name"]
    if email == 'gotten':
        email = data[code][0]["email"]

    emailReceiver = input('please enter email to receive your message: ')
    emailSender = 'textgames4@gmail.com'
    EMAIL_PASSWORD = 'iqtustjpidyswpgt' #dont change this or there will be an error coming up

    msg = EmailMessage()
    msg['Subject'] = 'text game save code'
    msg['From'] = emailSender
    msg['To'] = emailReceiver
    msg.set_content(f"""
    Hello {name}. Thank you for playing my game!
    Your save code is {code}.
    The password for this save file is {password}
    """)

    #files = [] #add file locations in here to send images
    #for thing in files:
    #    with open(thing,  'rb') as f:
    #        file_data = f.read()
    #        file_type = imghdr.what(f.name)
    #        file_name = f.name

    #    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(emailSender, EMAIL_PASSWORD)
        smtp.send_message(msg)