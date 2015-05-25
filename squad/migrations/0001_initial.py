# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import squad.models


class Migration(migrations.Migration):

    dependencies = [
        ('fixture', '0001_initial'),
        ('person', '0001_initial'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Squad',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('information', models.TextField()),
                ('squad_photo', models.ImageField(null=True, upload_to=squad.models.create_squad_photo_file_name, blank=True)),
                ('fixtures', models.ManyToManyField(null=True, to='fixture.Fixture', blank=True)),
                ('news_articles', models.ManyToManyField(null=True, to='news.NewsArticle', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SquadPersonRole',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('display_position', models.IntegerField()),
                ('person', models.OneToOneField(to='person.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SquadRole',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('information', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='squadpersonrole',
            name='role',
            field=models.OneToOneField(to='squad.SquadRole'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='squad',
            name='people',
            field=models.ManyToManyField(null=True, to='squad.SquadPersonRole', blank=True),
            preserve_default=True,
        ),
    ]
