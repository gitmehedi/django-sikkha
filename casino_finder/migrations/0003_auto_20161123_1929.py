# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casino_finder', '0002_citymodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Casino',
            new_name='CasinoModel',
        ),
        migrations.AlterModelOptions(
            name='casinomodel',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='citymodel',
            options={'ordering': ['name']},
        ),
    ]
