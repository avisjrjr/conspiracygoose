# Generated by Django 3.2.7 on 2021-09-09 20:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conspiracy',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 9, 9, 20, 33, 9, 54837, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='conspiracy',
            name='description',
            field=models.TextField(max_length=500000),
        ),
    ]