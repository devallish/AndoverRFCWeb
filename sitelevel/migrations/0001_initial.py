# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squad', '0004_auto_20150512_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='SquadMenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('display_name', models.CharField(max_length=20)),
                ('ordinal_position', models.IntegerField()),
                ('is_junior', models.BooleanField(default=True)),
                ('squad', models.OneToOneField(to='squad.Squad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
