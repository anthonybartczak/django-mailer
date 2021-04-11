from celery import Celery
from celery import shared_task
from celery.utils.log import get_task_logger
from .send_mail import mailgun_init

logger = get_task_logger(__name__)

app = Celery()

@app.task(name='mailing') 
def email_worker():
    mailgun_init()