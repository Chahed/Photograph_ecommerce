# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20151021_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titre', models.CharField(max_length=30, unique=True)),
                ('texte', models.TextField(null=True)),
                ('image', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
                ('projet', models.CharField(max_length=30, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='pictures',
        ),
    ]
