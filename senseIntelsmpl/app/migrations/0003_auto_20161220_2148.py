# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 05:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_module'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module',
            old_name='sensorName',
            new_name='moduleName',
        ),
        migrations.AlterField(
            model_name='gpsreading',
            name='altitude',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='gpsreading',
            name='latitude',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='gpsreading',
            name='longitude',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='gpsreading',
            name='speed',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='gpsreading',
            name='timeUtc',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='module',
            name='ipAddress',
            field=models.GenericIPAddressField(),
        ),
    ]
