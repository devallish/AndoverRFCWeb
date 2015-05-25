# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squadrole',
            name='information',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
