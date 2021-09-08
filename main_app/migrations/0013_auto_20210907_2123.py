# Generated by Django 3.2.7 on 2021-09-07 21:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20210907_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conspiracy',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 9, 7, 21, 23, 36, 469269, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='conspiracy',
            name='preview',
            field=models.CharField(default=datetime.datetime(2021, 9, 7, 21, 23, 36, 469228, tzinfo=utc), max_length=50),
        ),
    ]
