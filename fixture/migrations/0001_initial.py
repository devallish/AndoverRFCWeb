# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('opposition', models.CharField(max_length=50)),
                ('venue', models.CharField(max_length=50)),
                ('fixture_date', models.DateField()),
                ('meet_time', models.TimeField(null=True, blank=True)),
                ('kick_off_time', models.TimeField()),
                ('doofa', models.CharField(null=True, max_length=50, blank=True)),
                ('dress_code', models.CharField(null=True, max_length=50, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
