# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0001_initial'),
        ('squad', '0002_auto_20150510_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='squad',
            name='sponsors',
            field=models.ManyToManyField(blank=True, to='sponsor.Sponsor', null=True),
            preserve_default=True,
        ),
    ]
