# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20160921_0439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='vote',
            new_name='votes',
        ),
    ]
