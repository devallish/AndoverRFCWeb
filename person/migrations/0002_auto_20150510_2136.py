# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import person.models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=person.models.create_person_image_file_name),
            preserve_default=True,
        ),
    ]
