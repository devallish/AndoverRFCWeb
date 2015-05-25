# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import person.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('surname', models.CharField(max_length=50)),
                ('forenames', models.CharField(max_length=50)),
                ('email', models.EmailField(null=True, max_length=75, blank=True)),
                ('mobile', models.CharField(null=True, max_length=25, blank=True)),
                ('phone', models.CharField(null=True, max_length=25, blank=True)),
                ('image', models.ImageField(upload_to=person.models.create_person_image_file_name)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
