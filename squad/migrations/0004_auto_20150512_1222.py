# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fixture', '0002_auto_20150510_2136'),
        ('person', '0002_auto_20150510_2136'),
        ('squad', '0003_squad_sponsors'),
    ]

    operations = [
        migrations.CreateModel(
            name='SquadSelection',
            fields=[
                ('fixture', models.OneToOneField(serialize=False, to='fixture.Fixture', primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SquadSelectionItem',
            fields=[
                ('person', models.OneToOneField(serialize=False, to='person.Person', primary_key=True)),
                ('position_number', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='squadselection',
            name='players',
            field=models.ManyToManyField(to='squad.SquadSelectionItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='squad',
            name='selection',
            field=models.ManyToManyField(to='squad.SquadSelection', null=True, blank=True),
            preserve_default=True,
        ),
    ]
