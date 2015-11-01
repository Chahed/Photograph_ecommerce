# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='année',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
