# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-23 22:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_publicacion_grupo_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]