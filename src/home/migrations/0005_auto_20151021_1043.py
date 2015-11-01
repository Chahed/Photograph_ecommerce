# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_projet'),
    ]

    operations = [
        migrations.CreateModel(
            name='pictures',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(unique=True, max_length=30)),
                ('texte', models.TextField(null=True)),
                ('image', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
                ('projet', models.CharField(unique=True, max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='photo',
        ),
    ]
