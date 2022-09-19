from celery import shared_task
from apps.agent.utils import Send_sms

#----------------celery broker task---------------
@shared_task()
def send_sms(to_phone,opt):
    Send_sms(to_phone,opt)