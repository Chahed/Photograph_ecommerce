# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_client'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Client',
        ),
    ]
