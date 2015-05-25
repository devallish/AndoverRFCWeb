# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squad', '0004_auto_20150512_1222'),
        ('home', '0003_home_sponsors'),
    ]

    operations = [
        migrations.CreateModel(
            name='SquadMenuItem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=20)),
                ('ordinal_position', models.IntegerField()),
                ('squad', models.OneToOneField(to='squad.Squad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='home',
            name='junior_squad_menu_items',
            field=models.ManyToManyField(related_name='junior_home_id', null=True, blank=True, to='squad.Squad'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='home',
            name='senior_squad_menu_items',
            field=models.ManyToManyField(related_name='senior_home_id', null=True, blank=True, to='squad.Squad'),
            preserve_default=True,
        ),
    ]
