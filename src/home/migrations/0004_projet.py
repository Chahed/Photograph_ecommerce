# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20151021_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='projet',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('work', models.BooleanField(default=False)),
                ('titre', models.CharField(unique=True, max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
