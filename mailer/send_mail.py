from requests import post
from .models import EmailModel
from datetime import datetime, date
from .mailguncreds import MAILGUN_API_KEY, MAILGUN_BASE_URL
from django.conf import settings

def send_message(addresses, subject, content, image):
    return post(
        MAILGUN_BASE_URL + "/messages",
        auth=("api", MAILGUN_API_KEY),
        files={"inline":("image.png", open(image, mode='rb').read())},
        data={
            "from": "mailgun@sandboxa773e44539964739872c89c2c4a7cb73.mailgun.org",
            "to": addresses,
            "subject": subject,
            "html": '<html><div>' + content + '</div><div><img src="cid:image.png"></div></html>'})

def mailgun_init():
    
    current_hour = datetime.now().hour
    current_date = date.today()
    mails = EmailModel.objects.filter(date=current_date, hour=current_hour)

    if (len(mails) > 0):
        for mail in mails:
            address = mail.address.split(',')
            send_message(address, mail.title, mail.content, mail.image.path)
            print("Sending scheduled emails...")
    mails.delete()