# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-28 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0009_auto_20161228_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigationmenu',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]