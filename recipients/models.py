from django.db import models


class Recipient(models.Model):

    email = models.EmailField(verbose_name="Почта", help_text="Введите почту")
    full_name = models.CharField(max_length=200, verbose_name="ФИО", help_text="Введите ФИО")
    comment = models.TextField(verbose_name="Комментарий", help_text="Введите комментарий")

    class Meta:
        verbose_name = "Получатель"
        verbose_name_plural = "Получатели"

    def __str__(self):
        return self.full_name
