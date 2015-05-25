# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sponsor.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('summary', models.TextField(null=True, blank=True)),
                ('information', models.TextField(null=True, blank=True)),
                ('primary_url', models.URLField(null=True, blank=True)),
                ('secondary_url', models.URLField(null=True, blank=True)),
                ('primary_phone', models.CharField(null=True, max_length=25, blank=True)),
                ('secondary_phone', models.CharField(null=True, max_length=25, blank=True)),
                ('logo', models.ImageField(null=True, upload_to=sponsor.models.create_sponsor_image_filename, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
