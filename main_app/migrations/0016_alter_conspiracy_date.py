# Generated by Django 3.2.7 on 2021-09-07 21:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_auto_20210907_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conspiracy',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 9, 7, 21, 28, 7, 922013, tzinfo=utc)),
        ),
    ]