# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-23 18:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_album', models.CharField(max_length=30)),
                ('fecha_lanzamiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_artista', models.CharField(max_length=30)),
                ('apellidoP', models.CharField(max_length=30)),
                ('apellidoM', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_genero', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_grupo', models.CharField(max_length=30)),
                ('uploadfoto', models.FileField(upload_to='uploads/')),
                ('fecha_inicio', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='artista',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Grupo'),
        ),
        migrations.AddField(
            model_name='album',
            name='artista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Artista'),
        ),
    ]
