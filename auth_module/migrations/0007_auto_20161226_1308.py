# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-26 13:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0006_auto_20161226_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigationmenu',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_module.NavigationMenu'),
        ),
    ]
