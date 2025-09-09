from django.core.management.base import BaseCommand
from mailing.services import send_mailing

class Command(BaseCommand):
    help = 'Отправить рассылку'

    def add_arguments(self, parser):
        parser.add_argument('mailing_id', type=int)

    def handle(self, *args, **kwargs):
        mailing_id = kwargs['mailing_id']
        send_mailing(mailing_id)
        self.stdout.write(self.style.SUCCESS(f'Успешно отправленное почтовое отправление {mailing_id}'))
