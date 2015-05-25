# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('information', models.TextField()),
                ('event_date', models.DateTimeField()),
                ('news_article', models.OneToOneField(null=True, to='news.NewsArticle', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
