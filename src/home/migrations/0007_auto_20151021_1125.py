# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20151021_1101'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='picture',
            new_name='photo',
        ),
    ]
