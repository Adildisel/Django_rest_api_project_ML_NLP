# Generated by Django 2.2.6 on 2019-10-24 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20191024_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parsercomments',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ParserVideoId', verbose_name='Данные видео'),
        ),
    ]
