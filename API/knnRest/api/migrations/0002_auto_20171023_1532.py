# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 15:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='knnlist',
            old_name='firsDetail',
            new_name='firstDetail',
        ),
    ]
