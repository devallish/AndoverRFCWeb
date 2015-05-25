# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20150513_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squadmenuitem',
            name='squad',
        ),
        migrations.RemoveField(
            model_name='home',
            name='junior_squad_menu_items',
        ),
        migrations.RemoveField(
            model_name='home',
            name='senior_squad_menu_items',
        ),
        migrations.DeleteModel(
            name='SquadMenuItem',
        ),
    ]
