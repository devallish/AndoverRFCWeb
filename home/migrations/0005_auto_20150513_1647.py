# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20150513_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='junior_squad_menu_items',
            field=models.ManyToManyField(related_name='junior_home_id', null=True, blank=True, to='home.SquadMenuItem'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='home',
            name='senior_squad_menu_items',
            field=models.ManyToManyField(related_name='senior_home_id', null=True, blank=True, to='home.SquadMenuItem'),
            preserve_default=True,
        ),
    ]
