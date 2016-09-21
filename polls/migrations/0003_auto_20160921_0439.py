# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160921_0426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_text',
            new_name='title',
        ),
    ]
