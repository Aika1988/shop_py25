from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_activation_code(email, code):

    send_mail(
    'Py25 shop project', # title
    f'http://35.246.178.169/api/v1/account/activate/{code}', # body
    'ajkanysdzumagulova@gmail.com',
    [email]
    ) # to 
