# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GpsReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=50)),
                ('longitude', models.CharField(max_length=50)),
                ('timeUtc', models.CharField(max_length=50)),
                ('altitude', models.CharField(max_length=50)),
                ('speed', models.CharField(max_length=50)),
                ('climb', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SensorReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humidity', models.CharField(max_length=50)),
                ('temp', models.CharField(max_length=50)),
                ('pressure', models.CharField(max_length=50)),
                ('orient', models.CharField(max_length=50)),
                ('orientRaw', models.CharField(max_length=50)),
                ('compass', models.CharField(max_length=50)),
                ('compassRaw', models.CharField(max_length=50)),
                ('gyro', models.CharField(max_length=50)),
                ('gyroRaw', models.CharField(max_length=50)),
                ('accel', models.CharField(max_length=50)),
                ('accelRaw', models.CharField(max_length=50)),
            ],
        ),
    ]
