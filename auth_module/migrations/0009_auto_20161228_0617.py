# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-28 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0008_auto_20161227_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigationmenu',
            name='slug',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]