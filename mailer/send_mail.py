from requests import post
from .models import EmailModel
from datetime import datetime, date

current_hour = datetime.now().hour
current_date = date.today()
mails = EmailModel.objects.filter(date=current_date, hour=current_hour)


if (len(mails) > 0):
    for mail in mails:
        send_message(mail.address, mail.title, mail.content, mail.image)



def send_message(addresses, subject, content, image):
	return post(
		"https://api.mailgun.net/v3/sandboxa773e44539964739872c89c2c4a7cb73.mailgun.org/messages",
		auth=("api", "d4663b1aa6d7ec66e2383a43c5a052da-73e57fef-8ec9c2a6"),
		data={
            "from": "mailgun@sandboxa773e44539964739872c89c2c4a7cb73.mailgun.org",
			"to": addresses, #string array
			"subject": subject,
			"text": "Testing some Mailgun awesomness!"})
 