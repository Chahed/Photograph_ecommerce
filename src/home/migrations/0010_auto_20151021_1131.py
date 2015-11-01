# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_realisation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realisation',
            name='projet',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
