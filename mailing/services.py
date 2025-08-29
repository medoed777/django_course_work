import datetime

from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from mailing.models import Mailing
from message.models import Message


def start_sending_message(mailing: Mailing):
    report = []
    mailing.status_ending = Mailing.STATUS_STARTED
    mailing.save()
    for recipient in mailing.recipients.all():
        if not mailing.status_ending == "completed":
            message: Message = mailing.message
            try:
                send_mail(
                    subject=message.theme,
                    message=message.body,
                    recipient_list=[recipient.email],
                    from_email=EMAIL_HOST_USER,
                )
            except Exception as err:
                report.append(
                    f"{datetime.datetime.now()} - {recipient.email} ошибка - {err}"
                )
    mailing.status_ending = Mailing.STATUS_COMPLETED
    mailing.status_mail = "\n".join(report)
    mailing.save()
