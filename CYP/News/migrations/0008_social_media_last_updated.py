# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-09 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0007_auto_20180312_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='social_media',
            name='last_updated',
            field=models.DateTimeField(null=True),
        ),
    ]
