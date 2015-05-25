# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150507_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='news_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 10, 21, 36, 18, 836054)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='publish_date',
            field=models.DateField(default=datetime.date(2015, 5, 10)),
            preserve_default=True,
        ),
    ]
