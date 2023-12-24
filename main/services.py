from django.contrib.auth.models import Group, Permission
from django.core.mail import send_mail

from config import settings


def is_member(user):
    return user.groups.filter(name='moderator').exists()


def mail_sender(email):
    send_mail(
        subject='Course update',
        message='Course update',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=email
    )
