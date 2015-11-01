# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_remove_projet_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='commissioned_work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titre', models.CharField(max_length=30, unique=True)),
                ('image', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
