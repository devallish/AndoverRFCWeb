# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20150513_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='news_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 18, 15, 58, 16, 904206)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='publish_date',
            field=models.DateField(default=datetime.date(2015, 5, 18)),
            preserve_default=True,
        ),
    ]
