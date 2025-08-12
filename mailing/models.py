from django.db import models

from message.models import Message
from recipients.models import Recipient
from users.models import User


class Mailing(models.Model):

    STATUS_CREATED = "created"
    STATUS_STARTED = "started"
    STATUS_COMPLETED = "completed"

    STATUS_CHOICES = [
        (STATUS_CREATED, "Создана"),
        (STATUS_STARTED, "Запущена"),
        (STATUS_COMPLETED, "Завершена"),
    ]

    message = models.ForeignKey(
        Message, verbose_name="Сообщение", on_delete=models.CASCADE
    )
    recipients = models.ManyToManyField(Recipient, verbose_name="Получатели сообщения")
    status_ending = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_CREATED,
        verbose_name="Статус рассылки",
    )
    status_mail = models.TextField(verbose_name="Текстовый статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    owner = models.ForeignKey(
        User, verbose_name="Владелец рассылки", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        permissions = [
            ("can_all_view_mailing", "Просмотр всех рассылок"),
            ("can_delete_mailing", "Удаление рассылки"),
            ("can_update_mailing", "Обновление рассылки"),
            ("can_create_mailing", "Добавление рассылки"),
        ]