# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 03:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_module', '0002_auto_20161130_0209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctorbiomodel',
            options={'ordering': ['id'], 'verbose_name_plural': 'Doctors'},
        ),
    ]
