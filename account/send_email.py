from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
    'Py25 shop project', # title
    f'http://35.246.178.169/api/v1/account/activate/{code}', # body
    'ajkanysdzumagulova@gmail.com',
    [email]
    ) # to 


def send_reset_password_code(email, code):
    send_mail(
    'Py25 shop project', # title
    f'Привет чтобы сбросить пароль тебе нужно знать этот токен = {code}', # body
    'ajkanysdzumagulova@gmail.com',
    [email]
    ) # to 