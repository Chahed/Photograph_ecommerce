# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20151021_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='image',
            field=models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg'),
            preserve_default=True,
        ),
    ]
