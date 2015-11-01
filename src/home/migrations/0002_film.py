# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='film',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=30, unique=True)),
                ('texte', models.TextField(null=True)),
                ('image', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
