# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fixture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixture',
            name='kick_off_time',
            field=models.TimeField(choices=[(datetime.time(9, 0), '9:00 AM'), (datetime.time(10, 0), '10:00 AM'), (datetime.time(10, 30), '10:30 AM'), (datetime.time(11, 0), '11:00 AM'), (datetime.time(11, 30), '11:30 AM'), (datetime.time(12, 0), 'Midday'), (datetime.time(12, 30), '12:30 PM'), (datetime.time(13, 0), '1:00 PM'), (datetime.time(13, 30), '1:30 PM'), (datetime.time(14, 0), '2:00 PM'), (datetime.time(14, 30), '2:30 PM'), (datetime.time(15, 0), '3:00 PM')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fixture',
            name='meet_time',
            field=models.TimeField(choices=[(datetime.time(9, 0), '9:00 AM'), (datetime.time(10, 0), '10:00 AM'), (datetime.time(10, 30), '10:30 AM'), (datetime.time(11, 0), '11:00 AM'), (datetime.time(11, 30), '11:30 AM'), (datetime.time(12, 0), 'Midday'), (datetime.time(12, 30), '12:30 PM'), (datetime.time(13, 0), '1:00 PM'), (datetime.time(13, 30), '1:30 PM'), (datetime.time(14, 0), '2:00 PM'), (datetime.time(14, 30), '2:30 PM'), (datetime.time(15, 0), '3:00 PM')], blank=True, null=True),
            preserve_default=True,
        ),
    ]
