# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20151021_1125'),
    ]

    operations = [
        migrations.DeleteModel(
            name='photo',
        ),
    ]
