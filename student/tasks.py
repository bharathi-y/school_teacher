from celery import shared_task
from .models import Students

from django.core.mail import send_mail

from time import sleep

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_email_task():
    students = Students.objects.all()
    sleep(10)
    for student in students:
        send_mail('Celery Task Worked!',
        'This is proof the task worked!',
        'support@prettyprinted.com',
        [student.student_email])

    return None