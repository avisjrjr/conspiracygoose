# Generated by Django 3.2.7 on 2021-09-07 21:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_conspiracy_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conspiracy',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 9, 7, 21, 8, 51, 382512, tzinfo=utc)),
        ),
    ]
