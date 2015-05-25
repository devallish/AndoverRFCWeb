# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='news_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 7, 21, 41, 59, 616338)),
            preserve_default=True,
        ),
    ]
