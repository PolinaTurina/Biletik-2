# Generated by Django 4.2.1 on 2023-07-01 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0004_alter_otvet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otvet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='%y/%m/%d', verbose_name='Картинка'),
        ),
    ]