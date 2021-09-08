# Generated by Django 3.2.7 on 2021-09-07 21:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_auto_20210907_2128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conspiracy',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='conspiracy',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 9, 7, 21, 31, 18, 471072, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='conspiracy',
            name='preview',
            field=models.CharField(default='SOME STRING', max_length=50),
        ),
    ]
