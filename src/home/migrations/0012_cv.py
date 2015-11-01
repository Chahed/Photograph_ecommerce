# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_projet_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='cv',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='files/', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
