# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_remove_shop_annee'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='year',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
