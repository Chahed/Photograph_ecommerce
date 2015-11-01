# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_shop_année'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='année',
            new_name='annee',
        ),
    ]
