# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 01:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': 'user_info', 'verbose_name_plural': 'users_info'},
        ),
    ]