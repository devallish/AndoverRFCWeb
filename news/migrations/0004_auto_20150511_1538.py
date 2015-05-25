# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20150510_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='news_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 11, 15, 38, 44, 217230)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='publish_date',
            field=models.DateField(default=datetime.date(2015, 5, 11)),
            preserve_default=True,
        ),
    ]
