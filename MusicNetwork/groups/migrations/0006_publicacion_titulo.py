# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-23 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_auto_20160423_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='titulo',
            field=models.CharField(default='Sin titulo', max_length=30),
        ),
    ]
