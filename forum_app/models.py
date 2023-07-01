from django.db import models


class Tema(models.Model):
    title = models.CharField(max_length=32, verbose_name='Название темы')
    created_date=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания темы')

    class Meta:
        ordering = ['-id']
        verbose_name = ['Темы']
        verbose_name_plural = ['Темы']

    def __str__(self):
        return self.title


class Otvet(models.Model):
    name = models.CharField(max_length=32, verbose_name='Автор')
    text = models.CharField(max_length=2000, verbose_name="Текст ответа")
    image = models.ImageField(upload_to='%y/%m/%d', blank=True, null=True, verbose_name='Картинка')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_date']
        verbose_name = ['Ответ']
        verbose_name_plural = ['Ответы']

    def __str__(self):
        return self.name, self.text
