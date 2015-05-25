# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('headline', models.CharField(max_length=50)),
                ('summary', models.TextField(null=True, blank=True)),
                ('full_story', models.TextField()),
                ('news_date', models.DateTimeField(default=datetime.datetime(2015, 5, 7, 21, 20, 32, 558662))),
                ('publish_date', models.DateField(default=datetime.date(2015, 5, 7))),
                ('remove_date', models.DateField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
