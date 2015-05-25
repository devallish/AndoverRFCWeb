# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import news.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20150512_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='news_image',
            field=models.ImageField(blank=True, null=True, upload_to=news.models.get_news_image_filename),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='news_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 13, 7, 10, 12, 464091)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='publish_date',
            field=models.DateField(default=datetime.date(2015, 5, 13)),
            preserve_default=True,
        ),
    ]
