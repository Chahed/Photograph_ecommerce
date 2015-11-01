# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='ADRESS_LINE_1',
            new_name='ADDRESS_LINE_1',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='ADRESS_LINE_2',
            new_name='ADDRESS_LINE_2',
        ),
    ]
