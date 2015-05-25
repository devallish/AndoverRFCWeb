# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
        ('fixture', '0001_initial'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselItem',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('ordinal_position', models.IntegerField()),
                ('news_article', models.OneToOneField(to='news.NewsArticle')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50, default='Andover Rugby Club')),
                ('carousel_items', models.ManyToManyField(to='home.CarouselItem')),
                ('events', models.ManyToManyField(to='event.Event')),
                ('fixtures', models.ManyToManyField(to='fixture.Fixture')),
                ('news_articles', models.ManyToManyField(to='news.NewsArticle')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
