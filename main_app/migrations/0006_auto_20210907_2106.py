# Generated by Django 3.2.7 on 2021-09-07 21:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_conspiracy_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conspiracy',
            name='preview',
        ),
        migrations.AddField(
            model_name='conspiracy',
            name='title1',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conspiracy',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 9, 7, 21, 2, 51, 148783, tzinfo=utc)),
        ),
    ]