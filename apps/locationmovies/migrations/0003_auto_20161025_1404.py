# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 21:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locationmovies', '0002_auto_20161024_2157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='name',
            new_name='username',
        ),
    ]
