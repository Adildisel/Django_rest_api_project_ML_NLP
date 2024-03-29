# Generated by Django 2.2.6 on 2019-10-23 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ParserVideoId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель запроса')),
            ],
            options={
                'verbose_name': 'Данные видео',
                'verbose_name_plural': 'Данные видео',
            },
        ),
        migrations.CreateModel(
            name='ParserComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_comment', models.CharField(max_length=255, verbose_name='Автор комментария')),
                ('comment', models.TextField(verbose_name='Текст комментария')),
                ('assessment', models.CharField(max_length=255, verbose_name='Оценка коментария')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ParserVideoId', verbose_name='Данные видео')),
            ],
            options={
                'verbose_name': 'Данные комментариев',
                'verbose_name_plural': 'Данные комментариев',
            },
        ),
    ]
