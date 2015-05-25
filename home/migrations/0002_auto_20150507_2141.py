# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='carousel_items',
            field=models.ManyToManyField(null=True, to='home.CarouselItem', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='home',
            name='events',
            field=models.ManyToManyField(null=True, to='event.Event', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='home',
            name='fixtures',
            field=models.ManyToManyField(null=True, to='fixture.Fixture', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='home',
            name='news_articles',
            field=models.ManyToManyField(null=True, to='news.NewsArticle', blank=True),
            preserve_default=True,
        ),
    ]
