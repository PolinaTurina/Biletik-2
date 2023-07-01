from django.db import models


class Tema(models.Model):
    title = models.CharField(max_length=32, verbose_name='Название темы')
    created_date=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания темы')
